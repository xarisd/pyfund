"""Generators in Python

Generators:
    specify iterable sequences:
        all generators are iterators

    are lazily evaluated:
        the next value in the sequence is computed on demand

    can model infinite sequences:
        such as data streams with no definite end

    are composable into pipelines:
        for natural stream processing

"""

from utils import *


def gen123():
    yield 1
    yield 2
    yield 3
    return


def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")


def main():
    hrule("Create and use generator with next()")
    g = gen123()
    print("Generator execution returned:", end=" ")
    pp(g)
    pp(next(g))
    pp(next(g))
    pp(next(g))
    try:
        print("This is going to raise a StopIteration exception", end="...")
        pp(next(g))
    except StopIteration:
        print("Rescued it!")

    hrule("Use the generator as iterator")
    for v in gen123():
        print(v)

    hrule("Every call returns a NEW generator object")
    h = gen123()
    i = gen123()
    print("h : {}".format(h))
    print("i : {}".format(i))
    print("h is i : {}".format(h is i))
    print(next(h))
    print(next(h))
    print(next(i))

    hrule("How a generator is executed")
    g = gen246()
    next(g)
    next(g)
    next(g)
    try:
        print("This is going to raise a StopIteration exception", end="...\n")
        pp(next(g))
    except StopIteration:
        print("Rescued it!")


if __name__ == '__main__':
    main()