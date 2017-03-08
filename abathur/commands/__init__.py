# coding: utf8

import sys

from argparse import ArgumentParser

from .add_command import AddCommand
from .build_command import BuildCommand


DESCRIPTION = """
Abathur help you manage template and build project based on template.
"""


def get_parser():
    parser = AbathurParser(prog="abathur", description=DESCRIPTION)
    subparser = parser.add_subparsers()
    AddCommand().inject(subparser)
    BuildCommand().inject(subparser)
    return parser


class AbathurParser(ArgumentParser):
    def error(self, message):
        sys.stderr.write(f"error: {message}\n")
        self.print_help()
        sys.exit(2)
