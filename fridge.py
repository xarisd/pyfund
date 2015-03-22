"""Demonstrate raiding a refrigerator."""
from contextlib import closing


class RefrigeratorRaider:
    """Raid a refrigerator."""
    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning!")
        print("Taking {}".format(food))

    def close(self):
        print("Close fridge door.")


def raid(food):
    r = RefrigeratorRaider()
    r.open()
    try:
        r.take(food)
    finally:
        r.close()


def raid_with_closing(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)


if __name__ == '__main__':
    raid("Pizza")
    raid('deep fried pizza')
    raid_with_context_manager("Pizza")
    raid_with_context_manager('deep fried pizza')