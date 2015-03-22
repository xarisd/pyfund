"""Demonstration of Iteration Protocols

Iterable protocol:
    Iterable objects can be passed to the built-in
    iter() function to get an iterator.

    iterator = iter(iterable)

Iterator protocol:
    Iterator objects can be passed to the built-in
    next() function to fetch the next item.

    item = next(iterator)

"""

import sys


def print_items(iterable):
    iterator = iter(iterable)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass


def print_first(iterable):
    iterator = iter(iterable)
    try:
        print(next(iterator))
    except StopIteration:
        raise ValueError("iterable is empty")


def main():
    seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
    seasons_set = {'Spring', 'Summer', 'Autumn', 'Winter'}
    empty_list = []
    empty_set = set()

    print_items(seasons)
    print_items(seasons_set)
    print_items(empty_list)
    print_items(empty_set)
    print_first(seasons)
    print_first(seasons_set)
    print_first(empty_list)
    print_first(empty_set)

if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print("ValueError : {}".format(e), file=sys.stderr)