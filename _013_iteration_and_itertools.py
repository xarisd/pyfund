"""itertools usage examples

"""
from utils import *
from itertools import (islice, count)
from math import sqrt
from _011c_lucasseries import lucas


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def sum_of_x_prime_numbers(max_count=1000):
    thousand_primes = islice((x for x in count() if is_prime(x)), max_count)
    print(thousand_primes)
    s = sum(thousand_primes)
    print(s)


def any_or_all():
    _any = any([False, False, True])
    print(_any)
    _all = all([False, False, True])
    print(_all)
    _prime_between = any(is_prime(x) for x in range(1328, 1361))
    print(_prime_between)
    _all_cities_begin_with_a_capital = all(name == name.title() for name in ['London', 'New York', 'Sydney'])
    print(_all_cities_begin_with_a_capital)


def use_zip():
    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
    print("Sunday, Monday, Average")
    for sun, mon in zip(sunday, monday):
        av = (sun + mon) / 2.0
        print("{sun}, {mon}, {av}".format(sun=sun, mon=mon, av=av))


def use_zip_better():
    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
    tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]
    print(" Min, Max, Average")
    for temps in zip(sunday, monday, tuesday):
        print("{min:4.1f}, {max:4.1f}, {av:4.1f}".format(min=min(temps), max=max(temps), av=(sum(temps) / len(temps))))


def use_chain():
    from itertools import chain
    sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
    tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]
    temperatures = chain(sunday, monday, tuesday)
    _are_all_temperatures_over_zero = all(t >= 0 for t in temperatures)
    print(_are_all_temperatures_over_zero)


def main():
    hrule("Find the SUM of the first 1000 PRIME numbers")
    sum_of_x_prime_numbers(max_count=1000)
    hrule("Use of any() and all()")
    any_or_all()
    hrule("Use of zip()")
    use_zip()
    hrule("BETTER Use of zip()")
    use_zip_better()
    hrule("Use of chain()")
    use_chain()

    for x in (p for p in lucas() if is_prime(p)):
        print(x)


if __name__ == '__main__':
    main()