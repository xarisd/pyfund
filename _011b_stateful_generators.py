"""Stateful Generators and Lazy Evaluation

Generators:
    * Specify iterable sequences:
        all generators are iterators

    * Are lazily evaluated:
        the next value in the sequence is computed on demand

    * Can model infinite sequences:
        such as data streams with no definite end

    * Are composable into pipelines:
        for natural stream processing

    * Resume execution

    * Can maintain state in local variables

    * Can produce complex control flow

    * Are lazy evaluated

Laziness and the Infinite:
    * Just in Time Computation
    * Infinite (or large) sequences
    * Sensor readings
    * Mathematical series
    * Massive files
"""

from utils import *


def take(count, iterable):
    """Take items from the front of an iterable

    Args:
        count: The maximum number of items to retrieve.
        iterable: The source series.

    Yields:
        At most 'count' items from 'iterable'.
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """Return unique items by eliminating duplicates.

    Args:
        iterable: The source series.

    Yields:
        Unique elements in order from 'iterable'
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


def main():
    print(__doc__)
    hrule("Run take()")
    run_take()
    hrule("Run distinct()")
    run_distinct()
    hrule("Run pipeline take(3, distinct(items))")
    run_pipeline()


if __name__ == '__main__':
    main()