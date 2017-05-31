# coding: utf8

import os
import re
import shutil
import functools
import subprocess



class TemplateBuilder:
    def __init__(self, project, source, dest, placeholders, ignores):
        self.project = project
        self.source = source
        self.dest = dest
        self.placeholders = placeholders
        self.ignores = [re.compile(ignore_file) for ignore_file in ignores]

    def is_ignored(self, path):
        return any(
            [ignore.match(path) for ignore in self.ignores]
        )

    def copy_file(self, source, dest):
        if not self.is_ignored(source):
            print(f"copy: from {source} to {dest}")
            self._copy(source, dest)
            try:
                with open(source, "r") as f:
                    content = self.replace(f.read())
                    open(dest, "w").write(content)
            except Exception as e:
                print(f"copy file {source} error, {e}")

    def _copy(self, source, dest):
        def system_copy(command):
            p = subprocess.Popen(f"{command} {source} {dest}", stdout=subprocess.PIPE, shell=True)
            output, err = p.communicate()
            if err:
                print(err)

        if os.name in ("posix", "mac"):
            system_copy("cp")
        elif os.name == "nt":
            system_copy("copy")
        else:
            shutil.copy2(source, dest)


    def replace(self, src):
        return functools.reduce(
            lambda x, y: x.replace(y[0], y[1]),
            self.placeholders.items(),
            src
        )

    def make_dir(self, path, folder_name):
        dest = os.path.join(path, folder_name)
        if not self.is_ignored(dest):
            print(f"create dir {self.replace(dest)}")
            os.mkdir(self.replace(dest))

    def get_relative_path(self, src):
        return src.replace(self.source, "").lstrip("/")

    def get_dest(self, src):
        return os.path.join(self.dest, src)

    def build(self):
        if not os.path.exists(self.dest):
            os.mkdir(self.dest)
        for root, dirs, files in os.walk(self.source):
            dest = self.get_dest(self.get_relative_path(root))
            [self.copy_file(
                os.path.join(root, file_name),
                self.replace(os.path.join(dest, file_name))
            ) for file_name in files]
            [self.make_dir(dest, folder) for folder in dirs]
