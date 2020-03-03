'''
Calculate the runtime of the following recursive binary search function.

HINT:  
The function contains a subtle runtime bug due to memory management.
This bug causes the runtime to not be O(log n).
'''

def binary_search(xs, x):
    '''
    Returns whether x is contained in xs.

    >>> binary_search([0,1,3,4],1)
    True
    >>> binary_search([0,1,3,4],2)
    False
    '''
    mid = len(xs)//2
    if len(xs)==1:
        return xs[0]==x
    elif x<xs[mid]:
        return binary_search(xs[:mid],x)
    else:
        return binary_search(xs[mid:],x)
