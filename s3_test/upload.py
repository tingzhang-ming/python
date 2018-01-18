import os
import sys
import boto3


def env(key, default, environ=os.environ, fn=None):
    """
    Gets an environment variable, trims away comments and whitespace,
    and expands other environment variables.
    """
    val = environ.get(key, default)
    try:
        val = val.split('#')[0]
        val = val.strip()
        val = os.path.expandvars(val)
    except (AttributeError, IndexError):
        # just swallow AttributeErrors for non-strings
        pass
    if fn:  # transformation function
        val = fn(val)
    return val


def main(bucket, local_source_dir, remote_dir):
    s3 = boto3.resource('s3',
                        endpoint_url=None,
                        region_name='us-east-1',
                        aws_access_key_id=env('AWS_KEY_ID', ''),
                        aws_secret_access_key=env('AWS_SECRET_KEY', ''))
    # s3 = boto3.resource('s3',
    #                     endpoint_url='http://109.105.4.65:9001',
    #                     region_name='us-east-1',
    #                     aws_access_key_id='IW89KKUNNXT1LGSS6GLB',
    #                     aws_secret_access_key='3xCkdgO3TDjeFVfr7kFHMCRoip0BDzmnVxIeeMyv')
    for f in os.listdir(local_source_dir):
        with open(os.path.join(local_source_dir, f), 'rb') as data:
            s3.Bucket(bucket).put_object(Key=os.path.join(remote_dir, f), Body=data)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "usage: %s bucket local_source_dir remote_dir"
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
