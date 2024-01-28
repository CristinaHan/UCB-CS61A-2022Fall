"""https://inst.eecs.berkeley.edu/~cs61a/fa22/disc/disc01/"""

"""
Boolean Operators
·not returns the opposite boolean value of the following expression, 
 and will always return either True or False.
·and evaluates expressions in order and stops evaluating (short-circuits) once 
 it reaches the first falsy value, and then returns it. If all values evaluate to a truthy value, 
 the last value is returned.
·or evalutes expressions in order and short-circuits at the first truthy value and returns it. 
 If all values evaluate to a falsy value, the last value is returned.

"""

#Q1: Case Conundrum
'''What is the result of evaluating the following code?'''
def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

special_case()

'''12'''

def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

just_in_case()

'''19'''

def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x

case_in_point()

'''12'''

#Q2: Jacket Weather?
'''
Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
'''
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    if temp < 60 or raining:
        return True
    return False

#Q3: Square So Slow
'''What is the result of evaluating the following code?'''
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

square(so_slow(5))

'''Infinite loop'''

#Q4: Is Prime?
'''
Write a function that returns True if a positive integer n is a prime number
and False otherwise. 
'''
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    ans = 2
    while ans < n:
        if n % ans == 0:
            return False
        ans += 1
    return True

#Q5: Fizzbuzz
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    ans = 1
    while ans <= n:
        if ans % 3 == 0 and ans % 5 == 0 :
            print('fizzbuzz')
        elif ans % 3 == 0:
            print('fizz')
        elif ans % 5 == 0:
            print('buzz')
        else:
            print(ans)
        ans += 1

#Q6: Unique Digits
"""
Write a function that returns the number of unique digits in a positive integer.
"""
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    num = 0
    while n > 0:
        a = n % 10
        n //= 10
        if not has_digit(n, a):
            num += 1
    return num  


def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0:
        if n % 10 == k:
            return True
        n //= 10
    return False