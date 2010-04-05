# -*- encoding: utf-8 -*-

"""Fibonacci numbers using python generators/iterators
   :author: Milton Mazzarri
   :version: 0.1"""

def fibonacci():
    """
    Return the *Fibonacci number*

    Interesting bits:

    >>> fib = fibonacci()
    >>> fib.next()
    1
    >>> fib.next()
    1
    >>> fib.next()
    2
    >>> [fib.next() for i in range(10)]
    [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    :var first_seed: F\ :sub:`0`\  feed seed.
    :type first_seed: int
    :var second_seed: F\ :sub:`1`\  feed seed.
    :type second_seed: int
    :return: Return the `Fibonacci number`_
    :rtype: int

    .. _`Fibonacci number`: http://en.wikipedia.org/wiki/Fibonacci_number
    """
    first_seed = 0
    second_seed = 1

    while True:
        yield second_seed
        first_seed = second_seed
        second_seed = first_seed + second_seed

if __name__ == "__main__":
    import doctest
    doctest.testmod()
