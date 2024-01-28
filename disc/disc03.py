"""https://inst.eecs.berkeley.edu/~cs61a/fa22/disc/disc03/"""

"""
A recursive function is a function that is defined in terms of itself.
There are three main steps in a recursive definition:
·Base case. You can think of the base case as the case of the simplest function input,
 or as the stopping condition for the recursion.
·Recursive call on a smaller problem.You can think of this step as calling the function
 on a smaller problem that our current problem depends on. We assume that a recursive
 call on this smaller problem will give us the expected result; we call this idea the 
 "recursive leap of faith".
·Solve the larger problem. In step 2, we found the result of a smaller problem. We want
 to now use that result to figure out what the result of our current problem should be, 
 which is what we want to return from our current function call.
"""
#Q1: Warm Up: Recursive Multiplication
'''
Write a function that takes two numbers m and n and returns their product. 
Assume m and n are positive integers. Use recursion, not mul or *.
'''
def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    return multiply(m, n-1) + m


#Q3: Find the Bug
'''Find the bug with this recursive function.''' 
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:     # bug:漏了n为1时的base case
        return 1    
    elif n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)
    
#Q4: Is Prime
'''
Write a function is_prime that takes a single argument n and returns True if n is a prime number
and False otherwise. Assume n > 1. We implemented this in Discussion 1 iteratively, now time to 
do it recursively!
'''
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i):
        if i == n: 
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)


    
#Q5: Recursive Hailstone
'''
Recall the hailstone function from Homework 1. First, pick a positive integer n as the start. 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process 
until n is 1. Write a recursive version of hailstone that prints out the values of the sequence 
and returns the number of steps.
'''
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)

#Q6: Merge Numbers
def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
    