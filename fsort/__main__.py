import sys
import argparse

from .formatters import fsort

FORMATTERS = (fsort,)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="fsort",
        description=__doc__,
    )

    parser.add_argument(
        "filenames",
        nargs="+",
        help="filenames to check",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    filenames = list(set(args.filenames))
    error = False

    for formatter in FORMATTERS:
        error = formatter(filenames).format() or error

    return 1 if error else 0


if __name__ == "__main__":
    sys.exit(main())
