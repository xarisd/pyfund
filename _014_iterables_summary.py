"""Comprehensions, Generators & Iterables Summary

Comprehensions:

    * Comprehensions are a concise syntax for describing lists, sets and dictionaries

    * Comprehensions operate on an iterable source object and apply
      an optional predicate filter and a mandatory expression,
      both of which are usually in terms of the current item.

    * Iterables are objects over which we can iterate item by item.

    * We retrieve an iterator from an iterable object using the built-in iter() function.

    * Iterators produce items one-by-one from the underlying iterable series each time
      they are passed to the built-in next() function

Generators:

    * Generator functions allow us to describe series using imperative code.

    * Generator functions contain at least one use of the yield keyword

    * Generator are iterators. When advanced with next() the generator starts
      or resumes execution up to and including the next yield.

    * Each call to a generator function creates a new generator object.

    * Generators can maintain explicit state in local variables between iterations.

    * Generators are lazy, and so can model infinite series of data.

    * Generator expressions have a similar syntactic form to list comprehensions
      and allow for a more declarative and concise way of creating generator objects.

Iteration tools:
    * Built-ins such as:
        * sum()
        * any()
        * all()
        * zip()
        * min()
        * max()
        * enumerate()
    * Standard library itertools module
        * chain()
        * islice()
        * count()
        * many more!

"""


if __name__ == '__main__':
    print(__doc__)