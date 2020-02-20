def is_balanced_parens_1(xs,verbose=False):
    '''
    Takes a string as input and checks whether the parenthesis in the string are balanced.

    >>> is_balanced_parens_1('[[[(){}]()]]')
    True
    >>> is_balanced_parens_1('[[]')
    False
    '''
    xs = list(xs)
    for i in range(len(xs)-1):
        if verbose:
            print('i=',i,'xs=',''.join(xs))
        for j in range(len(xs)-1):
            if ( xs[j] == '(' and xs[j+1] == ')' ) or \
               ( xs[j] == '[' and xs[j+1] == ']' ) or \
               ( xs[j] == '{' and xs[j+1] == '}' ):
                del xs[j+1]
                del xs[j]
                break

    return len(xs)==0


def is_balanced_parens_2(xs,verbose=False):
    '''
    Improves on `is_balanced_parens_1` by using a while loop instead of a for loop

    >>> is_balanced_parens_2('[[[(){}]()]]')
    True
    >>> is_balanced_parens_2('[[]')
    False
    '''
    xs = list(xs)
    i = 0
    while i < len(xs)-1:
        if verbose:
            print('i=',i,'xs=',''.join(xs))
        for j in range(len(xs)-1):
            if ( xs[j] == '(' and xs[j+1] == ')' ) or \
               ( xs[j] == '[' and xs[j+1] == ']' ) or \
               ( xs[j] == '{' and xs[j+1] == '}' ):
                del xs[j+1]
                del xs[j]
                i-=1
                break
        i+=1

    return len(xs)==0


def is_balanced_parens_3(xs,verbose=False):
    '''
    Improves on `is_balanced_parens_2` by removing inner for loop

    >>> is_balanced_parens_3('[[[(){}]()]]')
    True
    >>> is_balanced_parens_3('[[]')
    False
    '''
    xs = list(xs)
    j = 0
    while len(xs) > 0 and j < len(xs)-1:
        if verbose:
            print('j=',j,'xs=',''.join(xs))
        if ( xs[j] == '(' and xs[j+1] == ')' ) or \
           ( xs[j] == '[' and xs[j+1] == ']' ) or \
           ( xs[j] == '{' and xs[j+1] == '}' ):
            del xs[j+1]
            del xs[j]
            j -= 1
        else:
            j += 1

    return len(xs)==0


import doctest
doctest.testmod()
