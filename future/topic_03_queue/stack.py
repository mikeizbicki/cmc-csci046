from collections import deque

def balanced_parens(text):
    '''
    Checks whether every ( has a matching ).

    Runtime in terms of a variable n;
    it will be a function of n.
    In this problem, n = len(text).

    >>> balanced_parens('')
    True
    >>> balanced_parens('(()())')
    True
    >>> balanced_parens('(()(()((()))))()(())')
    True
    >>> balanced_parens(')))(((')
    False
    >>> balanced_parens('(()()')
    False
    >>> balanced_parens('(()()))')
    False
    '''
    #stack = deque([])               # O(1)
    stack = {}
    size = 0
    for symbol in text:             # O(n) <- number of iterations
                                    #         and runtime
        if symbol == '(':           # O(1)
            stack[size] = symbol
            size += 1
            #stack.append(symbol)    # O(1)
        else:                       # O(1)
            #if len(stack) == 0:     # O(1)
            if size == 0:     # O(1)
                return False        # O(1)
            size -= 1
            del stack[size]
            #stack.pop()             # O(1)
    #if len(stack) == 0:             # O(1)
    if size == 0:             # O(1)
        return True                 # O(1)
    else:                           # O(1)
        return False                # O(1)

    # sum = O(n) = final runtime


def balanced_parens2(text):
    '''
    Checks whether all of the following types of parentheses are balanced: ([{

    >>> balanced_parens2('(()())')
    True
    >>> balanced_parens2('(()(()((()))))()(())')
    True
    >>> balanced_parens2('([]{})')
    True
    >>> balanced_parens2('([]{[][]{{()}}})')
    True
    >>> balanced_parens2('([}[})')
    False
    >>> balanced_parens2(')))(((')
    False
    >>> balanced_parens2('(()()')
    False
    >>> balanced_parens2('(()()))')
    False
    '''
    stack = []
    for symbol in text:
        if symbol in '([{' :
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            if (stack[-1] == '(' and symbol == ')') or \
               (stack[-1] == '[' and symbol == ']') or \
               (stack[-1] == '{' and symbol == '}'):
                stack.pop()
            else:
                return False
    return len(stack) == 0
