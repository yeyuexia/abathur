# coding: utf8

from abathur.command import get_parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    args.handle(args)
