'''
This document shows a general procedure for converting loops into recursive functions.
This procedure is useful because it is easier to analyze the runtime and correctness of recursive functions.

Given an iterative function

    def foo_iterative(params):
        header
        while condition:
            loop_body
        return tail

the following is an equivalent recursive function

    def foo_recursive(params):
        header
        def go(header_vars):
            if !condition:
                return tail
            loop_body
            return foo_recursive(header_vars_modified)
        return go(params, header_vars)

where header_vars is the set of variables defined in the header.
'''


def sum_iterative(xs):
    '''
    Returns the sum of the elements of the input list.

    >>> sum_iterative([1,2,3,4,5])
    15
    '''
    total = 0
    i = 0
    while i<len(xs):
        total += xs[i]
        i += 1
    return total


def sum_recursive(xs):
    '''
    Returns the sum of the elements of the input list.

    >>> sum_iterative([1,2,3,4,5])
    15
    '''
    i = 0
    total = 0
    def go(i, total):
        print('i=',i,'total=',total)
        if i<len(xs):
            return total
        total += xs[i]
        i += 1
        return go(i, total)
    return go(i, total)



def linear_search_iterative(xs,val):
    '''
    Returns an index satisfying `xs[index] == val`;
    if no such index exists, returns `None`.
    Makes no assumptions about the order of the input list.

    >>> linear_search_iterative(['a','b','c','d','e','f','g','h','i','j'],'d')
    3
    >>> linear_search_iterative(['a','b','c','d','e','f','g','h','i','j'],'j')
    9
    >>> linear_search_iterative(['a','b','c','d','e','f','g','h','i','j'],'a')
    0
    >>> linear_search_iterative(['a','b','c','d','e','f','g','h','i','j'],'k') is None
    True
    '''
    for i in range(len(xs)):
        if xs[i]==val:
            return i


def binary_search_iterative(xs, val):
    '''
    Returns an index satisfying `xs[index] == val`;
    if no such index exists, returns `None`.
    Assumes that the input list xs is in sorted order.

    >>> binary_search_iterative(['a','b','c','d','e','f','g','h','i','j'],'d')
    3
    >>> binary_search_iterative(['a','b','c','d','e','f','g','h','i','j'],'j')
    9
    >>> binary_search_iterative(['a','b','c','d','e','f','g','h','i','j'],'a')
    0
    >>> binary_search_iterative(['a','b','c','d','e','f','g','h','i','j'],'k') is None
    True
    '''
    left = 0
    right = len(xs)-1
    while left<=right:
        mid = (left+right)//2
        if val < xs[mid]:
            right = mid-1
        if val > xs[mid]:
            left = mid+1
        if val==xs[mid]:
            return mid
    return None

def binary_search_recursive(xs,val):
    '''
    Returns an index satisfying `xs[index] == val`;
    if no such index exists, returns `None`.
    Assumes that the input list xs is in sorted order.

    >>> binary_search_recursive(['a','b','c','d','e','f','g','h','i','j'],'d')
    3
    >>> binary_search_recursive(['a','b','c','d','e','f','g','h','i','j'],'j')
    9
    >>> binary_search_recursive(['a','b','c','d','e','f','g','h','i','j'],'a')
    0
    >>> binary_search_recursive(['a','b','c','d','e','f','g','h','i','j'],'k') is None
    True
    '''
    left = 0
    right = len(xs)-1
    def go(left,right):
        if left > right:
            return None
        mid = (left+right)//2
        if val < xs[mid]:
            right = mid-1
        if val > xs[mid]:
            left = mid+1
        if val==xs[mid]:
            return mid
        return go(left,right)
    return go(left,right)

