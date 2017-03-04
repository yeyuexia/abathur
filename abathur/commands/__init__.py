# coding: utf8

import sys

from argparse import ArgumentParser

from .alias_command import AliasCommand
from .build_command import BuildCommand


DESCRIPTION = """
Abathur help you build project based on template.
"""


def get_parser():
    parser = AbathurParser(prog="abathur", description=DESCRIPTION)
    subparser = parser.add_subparsers()
    AliasCommand().inject(subparser)
    BuildCommand().inject(subparser)
    return parser


class AbathurParser(ArgumentParser):
    def error(self, message):
        sys.stderr.write(f"error: {message}\n")
        self.print_help()
        sys.exit(2)
