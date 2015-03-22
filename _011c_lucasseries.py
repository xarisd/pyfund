"""Lucas series using Python Generators"""

from utils import *
from _011b_stateful_generators import take


def lucas():
    """Generate lucas series numbers.

    Yields:
        Items from Lucas series.
    """
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a+b


def print_lucas_up_to(count):
    """Prints lucas series number up to a specific count

    Args:
        count: The number of items to print
    """
    for i, item in enumerate(take(count, lucas())):
        print(i+1, item)


def main():
    print_lucas_up_to(50)


if __name__ == '__main__':
    main()