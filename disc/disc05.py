"""https://inst.eecs.berkeley.edu/~cs61a/fa22/disc/disc05/"""

#Q1: Map, Filter, Reduce
def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"
    return [fn(x) for x in seq]
def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    "*** YOUR CODE HERE ***"
    return [x for x in seq if pred(x)]

def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    total = seq[0]
    for subseq in seq[1:]:
        total = combiner(total, subseq)
    return total


#Q2: Count Palindromes
'''
Write a function that counts the number of palindromes (any string that reads the 
same forwards as it does when read backwards) in a sequence of strings using only 
lambda, string operations, conditional expressions, and the functions we defined 
above(my_filter, my_map, my_reduce). Specifically, do not use recursion or any k-
ind of loop.
'''
def count_palindromes(L):
    """The number of palindromic strings in the sequence of strings
    L (ignoring case).
    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    >>> count_palindromes(["101", "rAcECaR", "much", "wow"])
    3
    """
    return len(my_filter(lambda x: x[::-1].lower() == x.lower(), L))

#Q4: Height
def height(t):
    """Return the height of a tree. The height of a tree is the length 
    of the longest path from the root to a leaf.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])

#Q5: Maximum Path Sum
def max_path_sum(t):
    """Return the maximum path sum of the tree. A path is from the tree's 
    root to any leaf.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(branch) for branch in branches(t)])


#Q6: Find Path
'''
Write a function that takes in a tree and a value x and returns a list containing
the nodes along the path required to get from the root of the tree to a node con-
taining x.
'''
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for branch in branches(t):
        path = find_path(branch, x)
        if path:
            return [label(t)] + path

    
#Q7: Perfectly Balanced
'''
·Part A: Implement sum_tree, which returns the sum of all the labels in tree t.
·Part B: Implement balanced, which returns whether every branch of t has the same 
 total sum and that the branches themselves are also balanced.
·Challenge: Solve both of these parts with just 1 line of code each.
'''
def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
    #Challenge Solution
    return label(t) + sum(sum_tree(branch) for branch in branches(t))
    
    #Normal Solution
    #total = 0
    #for branch in branches(t):
        #total += sum_tree(branch)
    #return label(t) + total
    
def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    #Challenge Solution
    return all(sum_tree(branches(t)[0]) == sum_tree(branch) and balanced(branch) for branch in branches(t))
    
    #Normal Solution
    #for branch in branches(t):
        #if sum_tree(branches(t)[0]) != sum_tree(branch) or not balanced(branch):
            #return False
    #return True
    

#Q8: Hailstone Tree
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H.
    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
        2
            4
                8
                    16
    >>> print_tree(hailstone_tree(8, 3))
    8
        16
            32
                64
            5
                10
    """
    if h == 0:
        return tree(n)
    branches = ________________________________________
    if __________ and ______________ and ____________:
        branches += ____________________________________
    return tree(n, branches)

def print_tree(t):
    def helper(i, t):
        print("    " * i + str(label(t)))
        for b in branches(t):
            helper(i + 1, b)
    helper(0, t)


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)