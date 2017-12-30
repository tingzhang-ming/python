"""The Manta client."""
import sys
import logging
import json
import datetime
from . import errors
import requests


# ---- Python version compat

try:
    # Python 3
    from urllib.parse import urlencode
    from urllib.parse import quote as urlquote
except ImportError:
    # Python 2
    from urllib import urlencode
    from urllib import quote as urlquote

# ---- globals

log = logging.getLogger("manta.client")

# ---- compat

# Python version compat
# Use `bytes` for byte strings and `unicode` for unicode strings (str in Py3).
if sys.version_info[0] <= 2:
    py3 = False
    try:
        bytes
    except NameError:
        bytes = str
    base_string_type = basestring
elif sys.version_info[0] >= 3:
    py3 = True
    unicode = str
    base_string_type = str
    unichr = chr


DEFAULT_USER_AGENT = "samsung-dbcm-manta (%s) Python/%s" % (
    sys.platform, sys.version.split(None, 1)[0])


# ---- internal support stuff

def http_date(d=None):
    """Return HTTP Date format string for the given date.
    http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.3.1

    @param d {datetime.datetime} Optional. Defaults to `utcnow()`.
    """
    if not d:
        d = datetime.datetime.utcnow()
    return d.strftime("%a, %d %b %Y %H:%M:%S GMT")


# ---- exports

class RawMantaClient(object):
    """A raw client for accessing the Manta REST API. Here "raw" means that
    the API is limited to the strict set of endpoints in the REST API. No
    sugar. See the `MantaClient` subclass for the sugar.

    https://apidocs.joyent.com/manta/api.html
    https://apidocs.joyent.com/manta/pythonsdk/

    @param url {str} The Manta URL
    @param account {str} The Manta account (login name).
    @param subuser {str} Optional. The Manta sub user (login name).
    @param role {str} Optional. The Manta RBAC role.
    @param signer {Signer instance} A python-manta Signer class instance
        that handles signing request to Manta using the http-signature
        auth scheme.
    @param user_agent {str} Optional. User-Agent header string.
    @param cache_dir {str} Optional. A dir to use for HTTP caching. It will
        be created as needed.
    @param disable_ssl_certificate_validation {bool} Default false.
    @param verbose {bool} Optional. Default false. If true, then will log
        debugging info.
    """
    def __init__(self, url, account, subuser=None, role=None, sign=None,
                 signer=None, user_agent=None, cache_dir=None,
                 disable_ssl_certificate_validation=False,
                 verbose=False):
        assert account, 'account'
        if url.endswith('/'):
            self.url = url[:-1]
        else:
            self.url = url
        self.account = account
        self.subuser = subuser
        self.role = role
        self.signer = signer or sign
        self.user_agent = user_agent or DEFAULT_USER_AGENT
        self.disable_ssl_certificate_validation = disable_ssl_certificate_validation
        if verbose:
            global log
            log.setLevel(logging.DEBUG)
            import manta.auth
            manta.auth.log.setLevel(logging.DEBUG)

    def _request(self, path, method="GET", query=None, body=None, headers=None, stream=True):
        """Make a Manta request

        ...
        @returns (res, content)
        """
        assert path.startswith('/'), "bogus path: %r" % path

        # Presuming utf-8 encoding here for requests. Not sure if that is
        # technically correct.
        if isinstance(path, unicode):
            spath = path.encode('utf-8')
        else:
            spath = path

        qpath = urlquote(spath)
        if query:
            qpath += '?' + urlencode(query)
        url = self.url + qpath
        if headers is None:
            headers = {}
        headers["User-Agent"] = self.user_agent

        if self.signer:
            # Signature auth.
            if "Date" not in headers:
                headers["Date"] = http_date()
            sigstr = 'date: ' + headers["Date"]
            algorithm, fingerprint, signature = self.signer.sign(sigstr)
            auth = 'Signature keyId="/%s/keys/%s",algorithm="%s",signature="%s"'\
                   % ('/'.join(filter(None, [self.account, self.subuser])),
                      fingerprint, algorithm, signature)
            headers["Authorization"] = auth

            if self.role:
                headers['Role'] = self.role

        return requests.session().request(method=method,
                                          url=url,
                                          data=body,
                                          headers=headers,
                                          stream=stream,
                                          verify=not self.disable_ssl_certificate_validation)

    def put_directory(self, mdir):
        """PutDirectory
        https://apidocs.joyent.com/manta/api.html#PutDirectory

        @param mdir {str} A manta path, e.g. '/trent/stor/mydir'.
        """
        log.debug('PutDirectory %r', mdir)
        headers = {
            "Content-Type": "application/json; type=directory"
        }
        res = self._request(mdir, "PUT", headers=headers)
        if res.status_code != 204:
            raise errors.MantaAPIError(res, res.content)

    def list_directory(self, mdir, limit=None, marker=None):
        """ListDirectory
        https://apidocs.joyent.com/manta/api.html#ListDirectory

        @param mdir {str} A manta path, e.g. '/trent/stor/mydir'.
        @param limit {int} Limits the number of records to come back (default
            and max is 1000).
        @param marker {str} Key name at which to start the next listing.
        @returns Directory entries (dirents). E.g.:
            [{u'mtime': u'2012-12-11T01:54:07Z', u'name': u'play', u'type': u'directory'},
             ...]
        """
        res, dirents = self.list_directory2(mdir, limit=limit, marker=marker)
        return dirents

    def list_directory2(self, mdir, limit=None, marker=None):
        """A lower-level version of `list_directory` that returns the
        response object (which includes the headers).

        ...
        @returns (res, dirents) {2-tuple}
        """
        log.debug('ListDirectory %r', mdir)

        query = {}
        if limit:
            query["limit"] = limit
        if marker:
            query["marker"] = marker

        res = self._request(mdir, "GET", query=query)
        content = res.content
        if res.status_code != 200:
            raise errors.MantaAPIError(res, content)
        lines = content.splitlines(False)
        dirents = []
        for line in lines:
            if not line.strip():
                continue
            try:
                dirents.append(json.loads(line))
            except ValueError:
                raise errors.MantaError('invalid directory entry: %r' % line)
        return res, dirents

    def head_directory(self, mdir):
        """HEAD method on ListDirectory
        https://apidocs.joyent.com/manta/api.html#ListDirectory

        This is not strictly a documented Manta API call. However it is
        provided to allow access to the useful 'result-set-size' header.

        @param mdir {str} A manta path, e.g. '/trent/stor/mydir'.
        @returns The response object, which acts as a dict with the headers.
        """
        log.debug('HEAD ListDirectory %r', mdir)
        res = self._request(mdir, "HEAD")
        content = res.content
        if res.status_code != 200:
            raise errors.MantaAPIError(res, content)
        return res

    def delete_directory(self, mdir):
        """DeleteDirectory
        https://apidocs.joyent.com/manta/api.html#DeleteDirectory

        @param mdir {str} A manta path, e.g. '/trent/stor/mydir'.
        """
        log.debug('DeleteDirectory %r', mdir)
        res = self._request(mdir, "DELETE")
        content = res.content
        if res.status_code != 204:
            raise errors.MantaAPIError(res, content)

    def put_object(self, mpath, path=None, data=None,
                   content_type="application/octet-stream",
                   durability_level=None):
        """PutObject
        https://apidocs.joyent.com/manta/api.html#PutObject

        Examples:
            client.put_object('/trent/stor/foo', 'foo\nbar\nbaz')
            client.put_object('/trent/stor/foo', path='path/to/foo.txt')
            client.put_object('/trent/stor/foo', file=open('path/to/foo.txt'),
                              size=11)

        One of `content`, `path` or `file` is required.

        @param mpath {str} Required. A manta path, e.g. '/trent/stor/myobj'.
        @param path {str}
        @param data {bytes, iterator, dict}
        @param content_type {string} Optional, but suggested. Default is
            'application/octet-stream'.
        @param durability_level {int} Optional. Default is 2. This tells
            Manta the number of copies to keep.
        """
        log.debug('PutObject %r', mpath)
        headers = {
            "Content-Type": content_type,
        }
        if durability_level:
            headers["x-durability-level"] = durability_level

        methods = [m for m in [path, data] if m is not None]
        if len(methods) != 1:
            raise errors.MantaError("exactly one of 'content', 'path' or "
                                    "'file' must be provided")
        if path:
            content = open(path, 'rb')
        else:
            content = data
        res = self._request(mpath, "PUT", body=content,
                            headers=headers)
        if hasattr(content, 'close'):
            content.close()
        content = res.content
        if res.status_code != 204:
            raise errors.MantaAPIError(res, content)

    def get_object(self, mpath, path=None, accept="*/*", chunked=10485760, stream=True):
        """GetObject
        https://apidocs.joyent.com/manta/api.html#GetObject

        @param mpath {str} Required. A manta path, e.g. '/trent/stor/myobj'.
        @param path {str} Optional. If given, the retrieved object will be
            written to the given file path instead of the content being
            returned.
        @param accept {str} Optional. Default is '*/*'. The Accept header
            for content negotiation.
        @returns {str|None} None if `path` is provided, else the object
            content.
        """
        res = self.get_object2(mpath, accept=accept, stream=stream)
        if path:
            content = res.content
            with open(path, 'w') as pf:
                pf.write(content)
            if hasattr(res, 'close'):
                res.close()
            return res, content
        elif stream:
            return res, res.iter_content(chunk_size=10)
        else:
            content = res.content
            if hasattr(res, 'close'):
                res.close()
            return res, content

    def get_object2(self, mpath, accept="*/*", stream=True):
        """A lower-level version of `get_object` that returns the
        response object (which includes the headers).

        ...
        @returns (res, content) {2-tuple} `content` is None if `path` was
            provided
        """
        log.debug('GetObject %r', mpath)
        headers = {
            "Accept": accept
        }

        res = self._request(mpath, "GET", headers=headers, stream=stream)
        if res.status_code not in (200, 304):
            raise errors.MantaError('get object failed')
        return res

    # def get_object3(self, mpath, path=None, accept="*/*"):
    #     """A lower-level version of `get_object` that returns the
    #     response object (which includes the headers).
    #     """
    #     log.debug('GetObject %r', mpath)
    #     headers = {
    #         "Accept": accept
    #     }
    #
    #     res = self._request2(mpath, "GET", headers=headers)
    #     # content = res.content
    #     its = res.iter_content(chunk_size=10)
    #     for i in its:
    #         print i
    #     res.close()
    #     return ''
    #     # print '------------------------------------'
    #     # for k, v in vars(res).items():
    #     #     print k
    #     #     print v
    #     #     print '--------------------------------------'
    #     # if res.status_code not in (200, 304):
    #     #     raise errors.MantaError(content)
    #     # if len(content) != int(res.headers["content-length"]):
    #     #     raise errors.MantaError("content-length mismatch: expected %d, "
    #     #                             "got %s" % (res.headers["content-length"], content))
    #     # if res.headers.get("content-md5"):
    #     #     md5 = hashlib.md5(content)
    #     #     content_md5 = base64.b64encode(md5.digest())
    #     #     if content_md5 != res.headers["content-md5"]:
    #     #         raise errors.MantaError("content-md5 mismatch: expected %d, "
    #     #                                 "got %s" % (res.headers["content-md5"], content_md5))
    #     # if path is not None:
    #     #     f = open(path, 'wb')
    #     #     try:
    #     #         f.write(content)
    #     #     finally:
    #     #         f.close()
    #     #     return content
    #     # else:
    #     #     return content

    def delete_object(self, mpath):
        """DeleteObject
        https://apidocs.joyent.com/manta/api.html#DeleteObject

        @param mpath {str} Required. A manta path, e.g. '/trent/stor/myobj'.
        """
        log.debug('DeleteObject %r', mpath)
        res = self._request(mpath, "DELETE")
        content = res.content
        if res.status_code != 204:
            raise errors.MantaAPIError(res, content)
        return res

    def put_snaplink(self, link_path, object_path):
        """PutSnapLink
        https://mo.joyent.com/docs/muskie/master/api.html#putsnaplink

        @param link_path {str} Required. A manta path, e.g.
            '/trent/stor/mylink'.
        @param object_path {str} Required. The manta path to an existing target
            manta object.
        """
        log.debug('PutLink %r -> %r', link_path, object_path)
        headers = {
            "Content-Type": "application/json; type=link",
            "Location": object_path
        }
        res = self._request(link_path, "PUT", headers=headers)
        content = res.content
        if res.status_code != 204:
            raise errors.MantaAPIError(res, content)


class MantaClient(RawMantaClient):
    """A Manta client that builds on `RawMantaClient` to provide some
    API sugar.
    """
    get = RawMantaClient.get_object
    put = RawMantaClient.put_object
    rm = RawMantaClient.delete_object

    def ln(self, object_path, link_path):
        """Create a Manta link.

        This is a light wrapper around `put_snaplink`. Note, however, that the
        arguments *are* reversed so that `ln` is like the Unix command
        of the same name (i.e. the existing object is given first).

        @param object_path {str} Required. The manta path to an existing target
            manta object.
        @param link_path {str} Required. A manta path, e.g.
            '/trent/stor/mylink'.
        """
        return self.put_snaplink(link_path, object_path)

    def mkdir(self, mdir, parents=False):
        """Make a directory.

        Note that this will not error out if the directory already exists
        (that is how the PutDirectory Manta API behaves).

        @param mdir {str} A manta path, e.g. '/trent/stor/mydir'.
        @param parents {bool} Optional. Default false. Like 'mkdir -p', this
            will create parent dirs as necessary.
        """
        assert mdir.startswith('/'), "%s: invalid manta path" % mdir
        parts = mdir.split('/')
        assert len(parts) > 3, "%s: cannot create top-level dirs" % mdir
        if not parents:
            self.put_directory(mdir)
        else:
            # Find the first non-existant dir: binary search. Because
            # PutDirectory doesn't error on 'mkdir .../already-exists' we
            # don't have a way to detect a miss on `start`. So basically we
            # keep doing the binary search until we hit and close the `start`
            # to `end` gap.
            # Example:
            # - mdir: /trent/stor/builds/a/b/c  (need to mk a/b/c)
            #   parts: ['', 'trent', 'stor', 'builds', 'a', 'b', 'c']
            #   start: 4
            #   end: 8
            # - idx: 6
            #   d: /trent/stor/builds/a/b    (put_directory fails)
            #   end: 6
            # - idx: 5
            #   d: /trent/stor/builds/a   (put_directory succeeds)
            #   start: 5
            #   (break out of loop)
            # - for i in range(6, 8):
            #       i=6 -> d: /trent/stor/builds/a/b
            #       i=7 -> d: /trent/stor/builds/a/b/c
            end = len(parts) + 1
            start = 3  # Index of the first possible dir to create.
            while start < end - 1:
                idx = (end - start) / 2 + start
                d = '/'.join(parts[:idx])
                try:
                    self.put_directory(d)
                except errors.MantaAPIError:
                    _, ex, _ = sys.exc_info()
                    if ex.code == 'DirectoryDoesNotExist':
                        end = idx
                    else:
                        raise
                else:
                    start = idx

            # Now need to create from (end-1, len(parts)].
            for i in range(end, len(parts) + 1):
                d = '/'.join(parts[:i])
                self.put_directory(d)

    def mkdirp(self, mdir):
        """A convenience wrapper around mkdir a la `mkdir -p`, i.e. always
        create parent dirs as necessary.

        @param mdir {str} A manta path, e.g. '/trent/stor/mydir'.
        """
        return self.mkdir(mdir, parents=True)
