import hashlib
import os
import manta as pymanta
import logging as log

# MAX_FILE_SIZE = 2 * (1024 ** 3)
MAX_FILE_SIZE = 3 * 1024 * 1024
CHUNK_SIZE = 2 ** 4


class StreamReader(object):
    """Wrap the stream from the backup process and chunk it into segements."""

    def __init__(self, stream, filename, max_file_size=MAX_FILE_SIZE):
        self.stream = stream
        self.filename = filename
        self.container = self.filename
        self.max_file_size = max_file_size
        self.segment_length = 0
        self.process = None
        self.file_number = 0
        self.end_of_file = False
        self.end_of_segment = False
        self.segment_checksum = hashlib.md5()

    @property
    def base_filename(self):
        """Filename with extensions removed."""
        return self.filename.split('.')[0]

    @property
    def segment(self):
        return '%s_%08d' % (self.base_filename, self.file_number)

    @property
    def first_segment(self):
        return '%s_%08d' % (self.base_filename, 0)

    @property
    def segment_path(self):
        return '%s/%s' % (self.container, self.segment)

    def _read(self, chunk_size=CHUNK_SIZE):
        if self.end_of_segment:
            self.segment_length = 0
            self.segment_checksum = hashlib.md5()
            self.end_of_segment = False

        # Upload to a new file if we are starting or too large
        if self.segment_length > (self.max_file_size - chunk_size):
            self.file_number += 1
            self.end_of_segment = True
            return ''

        chunk = self.stream.read(chunk_size)
        if not chunk:
            self.end_of_file = True
            return ''

        self.segment_checksum.update(chunk)
        self.segment_length += len(chunk)
        return chunk

    def read(self):
        result = ''
        current_file_number = self.file_number
        while self.file_number == current_file_number:
            result += self._read()
            if self.end_of_file:
                break
        return result


class MantaStorage(pymanta.MantaClient):
    """ Improve manta client to support stream """

    def __init__(self, *args, **kwargs):
        super(MantaStorage, self).__init__(*args, **kwargs)

    def put_object(self, mpath, content=None, path=None, file=None,
                   content_length=None,
                   content_type="application/octet-stream",
                   durability_level=None):
        """ Persist information from the stream to manta. """
        filename = os.path.basename(mpath)
        stream_reader = StreamReader(file, filename, MAX_FILE_SIZE)
        log.debug('Using segment size %s', stream_reader.max_file_size)
        segment_results = []
        self.mkdir(mpath)
        while not stream_reader.end_of_file:
            log.debug('Saving segment %s.', stream_reader.segment)
            path = os.path.join(mpath, stream_reader.segment)
            super(MantaStorage, self).put_object(path, file=stream_reader)
            # content = stream_reader.read()
            # print type(content)
            segment_results.append({
                'path': path,
                'size_bytes': stream_reader.segment_length
            })
        # All segments uploaded.
        num_segments = len(segment_results)
        log.debug('File uploaded in %s segments.', num_segments)

    # def _explodeLocation(self, location):
    #     storage_url = "/".join(location.split('/')[:-2])
    #     container = location.split('/')[-2]
    #     filename = location.split('/')[-1]
    #     return storage_url, container, filename
    #
    # def _verify_checksum(self, etag, checksum):
    #     etag_checksum = etag.strip('"')
    #     if etag_checksum != checksum:
    #         msg = (_("Original checksum: %(original)s does not match"
    #                  " the current checksum: %(current)s") %
    #                {'original': etag_checksum, 'current': checksum})
    #         LOG.error(msg)
    #         raise SwiftDownloadIntegrityError(msg)
    #     return True
    #
    # def load(self, location, backup_checksum):
    #     """Restore a backup from the input stream to the restore_location."""
    #     storage_url, container, filename = self._explodeLocation(location)
    #
    #     headers, info = self.connection.get_object(container, filename,
    #                                                resp_chunk_size=CHUNK_SIZE)
    #
    #     if CONF.verify_swift_checksum_on_restore:
    #         self._verify_checksum(headers.get('etag', ''), backup_checksum)
    #
    #     return info
    #
    # def _get_attr(self, original):
    #     """Get a friendly name from an object header key."""
    #     key = original.replace('-', '_')
    #     key = key.replace('x_object_meta_', '')
    #     return key
    #
    # def _set_attr(self, original):
    #     """Return a swift friendly header key."""
    #     key = original.replace('_', '-')
    #     return 'X-Object-Meta-%s' % key
    #
    # def load_metadata(self, location, backup_checksum):
    #     """Load metadata from swift."""
    #
    #     storage_url, container, filename = self._explodeLocation(location)
    #
    #     headers = self.connection.head_object(container, filename)
    #
    #     if CONF.verify_swift_checksum_on_restore:
    #         self._verify_checksum(headers.get('etag', ''), backup_checksum)
    #
    #     _meta = {}
    #     for key, value in headers.items():
    #         if key.startswith('x-object-meta'):
    #             _meta[self._get_attr(key)] = value
    #
    #     return _meta
    #
    # def save_metadata(self, location, metadata={}):
    #     """Save metadata to a swift object."""
    #
    #     storage_url, container, filename = self._explodeLocation(location)
    #
    #     headers = {}
    #     for key, value in metadata.items():
    #         headers[self._set_attr(key)] = value
    #
    #     LOG.info(_("Writing metadata: %s"), str(headers))
    #     self.connection.post_object(container, filename, headers=headers)
