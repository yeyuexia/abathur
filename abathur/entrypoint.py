# coding: utf8

from abathur.commands import get_parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    print(dir(args))
    args.handle(args)
