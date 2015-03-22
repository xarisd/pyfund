"""Generator Comprehensions

    * Similar syntax to list comprehensions
    * Create a generator object
    * Concise
    * Lazy evaluation
"""
from utils import *


def is_odd(x):
    return x % 2 == 1


def main():
    hrule("Create a generator comprehension")
    million_squares = (x*x for x in range(1, 1000001))
    print(million_squares)

    hrule("Create a list from generator comprehension (almost 40MB of RAM required)")
    as_a_list = list(million_squares)
    print(type(as_a_list))

    hrule("The generator is now empty! Creating another list from this generator will return an EMPTY LIST")
    as_a_second_list = list(million_squares)
    print(as_a_second_list)

    hrule("Use the sum() to produce the SUM of 1.000.000 square numbers, with generator comprehension")
    s = sum(x*x for x in range(1, 1000001))
    print(s)

    hrule("You can use generator comprehension with filter clause")
    s = sum(x for x in range(1000000) if is_odd(x))
    print(s)


if __name__ == '__main__':
    main()