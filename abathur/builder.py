# coding: utf8

import os
import re
import shutil

from os import path, mkdir
from functools import reduce


class TemplateBuilder:
    __IGNORE_FILES__ = [r"\.git/.*", r".abathur"]

    def __init__(self, project, source, dest, placeholders):
        self.project = project
        self.source = source
        self.dest = dest
        self.placeholders = placeholders
        self.ignores = [re.compile(ignore_file) for ignore_file in self.__IGNORE_FILES__]

    def is_ignored(self, path):
        return any(
            [ignore.match(path) for ignore in self.ignores]
        )

    def copy_file(self, source, dest):
        if not self.is_ignored(folder_name):
            print(f"copy: from {source} to {dest}")
            shutil.copyfile(source, dest)
            try:
                with open(source, "r") as f:
                    open(dest, "w").write(self.replace(f.read()))
            except Exception e:
                print(f"copy file {source} error, {e}")

    def replace(self, src):
        return reduce(
            lambda x, y: x.replace(y[0], y[1]),
            self.placeholders.items(),
            src
        )

    def make_dir(self, dest, folder_name):
        if not self.is_ignored(folder_name):
            print(f"create dir {self.replace(path.join(dest, folder_name))}")
            mkdir(self.replace(path.join(dest, folder_name)))

    def get_relative_path(self, src):
        return src.replace(self.source, "").lstrip("/")

    def get_dest(self, src):
        return path.join(self.dest, src)

    def build(self):
        mkdir(self.dest)
        for root, dirs, files in os.walk(self.source):
            dest = self.get_dest(self.get_relative_path(root))
            [self.copy_file(
                path.join(root, file_name),
                self.replace(path.join(dest, file_name))
            ) for file_name in files]
            [self.make_dir(dest, folder) for folder in dirs]
