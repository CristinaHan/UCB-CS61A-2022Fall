"""https://inst.eecs.berkeley.edu/~cs61a/fa22/disc/disc04/"""

#Q1: Count Stair Ways
'''
Imagine that you want to go up a flight of stairs that has n steps, where n is 
a positive integer. You can either take 1 or 2 steps each time. How many diff-
erent ways can you go up this flight of stairs? In this question, you'll write 
a function count_stair_ways that solves this problem.
'''
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return count_stair_ways(n-1) + count_stair_ways(n-2)

#Q2: Count K
'''
Consider a special version of the count_stair_ways problem, where instead of taking
1 or 2 steps, we are able to take up to and including k steps at a time. Write a f-
unction count_k that figures out the number of paths for this scenario. Assume n and
k are positive.
'''
def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total

#Q4: Even weighted
'''
Write a function that takes a list s and returns a new list that keeps only the 
even-indexed elements of s and multiplies them by their corresponding index.
'''
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]

#Q5: Max Product
'''
Write a function that takes in a list and returns the maximum product that can be 
formed using nonconsecutive elements of the list. The input list will contain only 
numbers greater than or equal to 1.
'''
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1
    else:
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))
