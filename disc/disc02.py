"""https://inst.eecs.berkeley.edu/~cs61a/fa22/disc/disc02/"""

#Q5: Make Keeper
"""
Write a function that takes in a number n and returns a function that can take in a single parameter cond.
When we pass in some condition function cond into this returned function, 
it will print out numbers from 1 to n where calling cond on that number returns True.
"""

def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    def keeper(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)

    return keeper