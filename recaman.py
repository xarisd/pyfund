import sys
from itertools import (count, islice)


def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    a = 0
    for n in count():
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """Write Recaman's sequence to a text file."""
    f = open(filename, mode='wt', encoding='utf-8')
    f.writelines("{0}\n".format(r)
                 for r in islice(sequence(), num + 1))
    f.close()


def write_sequence_with_try_block(filename, num):
    """Write Recaman's sequence to a text file."""
    try:
        f = open(filename, mode='wt', encoding='utf-8')
        f.writelines("{0}\n".format(r)
                     for r in islice(sequence(), num + 1))
    finally:
        f.close()


def write_sequence_with_context_manager(filename, num):
    """Write Recaman's sequence to a text file."""
    with open(filename, mode='wt', encoding='utf-8') as f:
        f.writelines("{0}\n".format(r)
                     for r in islice(sequence(), num + 1))


if __name__ == '__main__':
    write_sequence_with_context_manager(filename=sys.argv[1], num=int(sys.argv[2]))