'''
This file contains two techniques for checking if a string is a palindrome.
They have different runtimes depending on which data structures are used.

Palindrome checking is a classic "leetcode easy" problem for interviews.
See: <https://leetcode.com/problems/valid-palindrome/>.
'''

import copy
from collections import deque


def check_palindrome_1(container):
    '''
    checks whether the input container reads the same forwards as it does backwards

    >>> check_palindrome_1('abcdcba')
    True
    >>> check_palindrome_1('abcd')
    False

    >>> check_palindrome_1(['a', 'b', 'c', 'd', 'c', 'b', 'a'])
    True
    >>> check_palindrome_1(['a', 'b', 'c', 'd'])
    False

    >>> check_palindrome_1(deque(['a', 'b', 'c', 'd', 'c', 'b', 'a']))
    True
    >>> check_palindrome_1(deque(['a', 'b', 'c', 'd']))
    False
    '''
    for i in range(len(container)//2):
        left = container[i]
        right = container[len(container)-1-i]
        if left != right:
            return False
    return True


def check_palindrome_2(container):
    '''
    checks whether the input container reads the same forwards as it does backwards

    >>> check_palindrome_2('abcdcba')
    True
    >>> check_palindrome_2('abcd')
    False

    >>> check_palindrome_2(['a', 'b', 'c', 'd', 'c', 'b', 'a'])
    True
    >>> check_palindrome_2(['a', 'b', 'c', 'd'])
    False

    >>> check_palindrome_2(deque(['a', 'b', 'c', 'd', 'c', 'b', 'a']))
    True
    >>> check_palindrome_2(deque(['a', 'b', 'c', 'd']))
    False
    '''

    # this line converts the input container into an equivalent deque;
    # converting from one form of a container into another has the runtime
    # of performing a copy on the container you are converting into
    container_copy = deque(container)
    
    for i in range(len(container)//2):
        left = container_copy.popleft()
        right = container_copy.pop()
        if left != right:
            return False
    return True
