# coding: utf8

import os
import shutil
import argparse

from os import path, mkdir
from functools import reduce


DEFAULT_TEMPLATE_PATH = "template"


class Builder:

    def __init__(self, project, source, dest, placeholders, configuration):
        self.project = project
        self.source = source
        self.dest = dest
        self.placeholders = self._init_placeholders(
            placeholders, configuration
        )

    def _init_placeholders(self, src, configuration):
        placeholders = dict()
        placeholders["{PROJECT_NAME}"] = self.project
        if configuration:
            with open(configuration, "r") as f:
                placeholders.update(
                    [self.parse_placeholder(row) for row in f.readlines()]
                )
        placeholders.update([self.parse_placeholder(val) for val in src])
        return placeholders

    def parse_placeholder(self, src):
        key, value = src.split("=")
        return "{" + key.strip() + "}", value.strip()

    def copy_file(self, source, dest):
        print("copy " + source + " to " + dest)
        shutil.copyfile(source, dest)
        try:
            with open(source, "r") as f:
                open(dest, "w").write(self.replace(f.read()))
        except Exception:
            pass

    def replace(self, src):
        return reduce(
            lambda x, y: x.replace(y[0], y[1]),
            self.placeholders.items(),
            src
        )

    def make_dir(self, dest, folder_name):
        print("create dir " + self.replace(path.join(dest, folder_name)))
        mkdir(self.replace(path.join(dest, folder_name)))

    def get_relative_path(self, src):
        return src.replace(self.source, "").lstrip("/")

    def get_dest(self, src):
        return path.join(self.dest, src)

    def build(self):
        mkdir(self.dest)
        for root, dirs, files in os.walk(template_path):
            dest = self.get_dest(self.get_relative_path(root))
            [self.copy_file(
                path.join(root, file_name),
                self.replace(path.join(dest, file_name))
            ) for file_name in files]
            [self.make_dir(dest, folder) for folder in dirs]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="build project based on template"
    )
    parser.add_argument("project_name", metavar="project_name")
    parser.add_argument("-t", "--template", metavar="template path")
    parser.add_argument("-o", "--output", metavar="output path")
    parser.add_argument(
        "-p", "--placeholder",
        metavar="--placeholder {placeholder}={what_your_want_replace}",
        default=""
    )
    parser.add_argument(
        "-f", "--file",
        metavar="--file configuration_file", default=None
    )
    args = parser.parse_args()

    template_path = args.template or DEFAULT_TEMPLATE_PATH
    dest_root = args.output or args.project_name
    Builder(
        args.project_name, template_path, dest_root,
        args.placeholder, args.file
    ).build()
