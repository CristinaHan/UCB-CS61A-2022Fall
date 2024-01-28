"""https://inst.eecs.berkeley.edu/~cs61a/fa22/disc/disc08/"""

#Q3: Sum Nums
'''Write a function that takes in a linked list and returns the sum of all its elements. 
You may assume all elements in s are integers. Try to implement this recursively!
'''
def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** YOUR CODE HERE ***"
    if s is Link.empty:
        return 0
    return s.first + sum_nums(s.rest)


#Q4: Multiply Links
'''Write a function that takes in a Python list of linked lists and multiplies them 
element-wise. It should return a new linked list.

If not all of the Link objects are of equal length, return a linked list whose length
is that of the shortest linked list given. You may assume the Link objects are shall-
ow linked lists, and that lst_of_lnks contains at least one linked list.
'''
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    new_first = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        new_first *= lnk.first
    new_lst_of_lnks = [lnk.rest for lnk in lst_of_lnks]
    return Link(new_first, multiply_lnks(new_lst_of_lnks))


#Q5: Flip Two
'''Write a recursive function flip_two that takes as input a linked list s and
mutates s so that every pair is flipped.
'''
def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    "*** YOUR CODE HERE ***"
    if s is Link.empty or s.rest is Link.empty:
        return 
    s.first, s.rest.first = s.rest.first, s.first
    flip_two(s.rest.rest)

    # For an extra challenge, try writing out an iterative approach as well below!
    "*** YOUR CODE HERE ***"
    while s is not Link.emptys and s.rest is not Link.empty:
        s.first, s.rest.first = s.rest.first, s.first
        s = s.rest.rest


#Q6: Make Even
'''Define a function make_even which takes in a tree t whose values are 
integers, and mutates the tree such that all the odd integers are increased 
by 1 and all the even integers remain the same.
'''
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    "*** YOUR CODE HERE ***"
    if t.label % 2 != 0:
        t.label += 1
    for b in t.branches:
        make_even(b)

#Q7: Add Leaves
def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>> t_one_to_four = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> print(t_one_to_four)
    1
      2
      3
        4
    >>> add_d_leaves(t_one_to_four, 5)
    >>> print(t_one_to_four)
    1
      2
        5
      3
        4
          5
          5
        5

    >>> t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> print(t3)
    3
      1
        3
          4
      0
      2
        5
        6
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    "*** YOUR CODE HERE ***"
    def add_leaves(t, d):
        for b in t.branches:
            add_leaves(b, d + 1)
        t.branches.extend([Tree(v) for _ in range(d)])
    add_leaves(t, 0)



class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches