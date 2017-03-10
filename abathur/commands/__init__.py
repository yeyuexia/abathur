# coding: utf8

import sys

from argparse import ArgumentParser

from .add_command import AddCommand
from .build_command import BuildCommand
from .list_command import ListCommand
from .remove_command import RemoveCommand


DESCRIPTION = """
Abathur help you manage template and build project based on template.
"""


def get_parser():
    parser = AbathurParser(prog="abathur", description=DESCRIPTION)
    parser.load_subparsers()
    return parser


class AbathurParser(ArgumentParser):
    sub_commands = [AddCommand, BuildCommand, ListCommand, RemoveCommand]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def load_subparsers(self):
        subparser = self.add_subparsers()
        [sub_command().inject(subparser) for sub_command in self.sub_commands]

    def error(self, message):
        sys.stderr.write(f"error: {message}\n")
        self.print_help()
        sys.exit(2)
