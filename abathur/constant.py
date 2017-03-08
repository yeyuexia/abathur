# coding: utf8

from os import path

ABATHUR_CONFIGURATION_ROOT = path.join(path.expanduser("~"), ".abathur")
ALIAS_CONFIGURATION = path.join(ABATHUR_CONFIGURATION_ROOT, "alias.json")
ABATHUR_CONFIGURATION = ".abathur"
IGNORE_FILES = [r"(.*/)?\.git.*", r"(.*/)?.abathur"]
REMOTE_RESOURCE_HEADER = [r"^(https://|ssh://|http://)?(git@)?.*\.git$"]
LOCAL_RESOURCE = "__local_resource__"
REMOTE_RESOURCE = "__remote_resource__"
