
import hashlib
import os

print hashlib.sha1(os.urandom(24)).hexdigest()

