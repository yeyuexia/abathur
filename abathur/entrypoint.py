# coding: utf8

import sys

from abathur.commands import get_parser
from abathur.abathur import prepare_environment


if __name__ == "__main__":
    prepare_environment()
    parser = get_parser()
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()
    args = get_parser().parse_args()
    args.handle(args)
