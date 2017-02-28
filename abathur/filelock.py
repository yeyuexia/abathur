# coding: utf8

import os
import errno
import time


class FileLock:
    def __init__(self, resource, timeout=1, delay=0.01):
        self.resource = resource
        self.timeout = timeout
        self.delay = delay

    def __enter__(self):
        waiting_time = 0
        while True:
            try:
                self.lock_fd = os.open(
                    f"{self.resource}.lock", os.O_CREAT | os.O_EXCL | os.O_RDWR
                )
                break
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise e
                waiting_time += self.delay
                if waiting_time > self.timeout:
                    raise LockTimeoutException(
                        self.resource, self.timeout
                    )
                time.sleep(self.delay)
            self.fd = open(self.resource)
        return self.fd

    def __exit__(self, type, value, traceback):
        os.close(self.lock_fd)
        os.unlink(self.lock_fd)
        os.close(self.fd)