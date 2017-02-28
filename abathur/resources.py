# coding: utf8

import os
import os.path

from .filelock import FileLock


class LockTimeoutException(Exception):
    def __init__(self, resource, timeout):
        self.resource = resource
        self.timeout = timeout

    def __repr__(self):
        return f"try open lock file {self.resource} timeout. time: {self.timeout}"

class NotSupportException(Exception):
    pass

def require(resource):
    return FileLock(resource)


__REMOTE_RESOURCE_HEADER__ = ["git@", "https://"]
LOCAL_RESOURCE = "__local_resource__"
REMOTE_RESOURCE = "__remote_resource__"
def get_resource_type(resource):
    if os.path.exists(resource):
        return LOCAL_RESOURCE
    elif resource.startswith(__REMOTE_RESOURCE_HEADER__):
        return REMOTE_RESOURCE
    raise NotSupportException()
