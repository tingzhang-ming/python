"""A Python client/CLI/shell/SDK for Joyent Manta."""

from .client import MantaClient
from .auth import PrivateKeySigner, SSHAgentSigner, CLISigner
from .errors import *
