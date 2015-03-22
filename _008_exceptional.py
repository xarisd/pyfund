"""A module for demonstrating exceptions."""

import sys
from math import log


def convert(x):
    """Convert to an integer."""
    try:
        return int(x)
        # print("Conversion succeeded! x=", x)
    except (ValueError, TypeError) as e:
        print("Conversion failed : {}".format(str(e)), file=sys.stderr)
        raise


def string_log(s):
    v = convert(s)
    return log(v)


def main():
    print(convert("100"))
    print(convert("bla"))


if __name__ == '__main__':
    main()
