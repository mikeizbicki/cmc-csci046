'''
This is the code the book uses to balance parentheses in Section 4.5-4.7

Pythonic == good code
'''

def par_checker(symbol_string):
    '''
    >>> par_checker('{({([][])}())}')
    True
    >>> par_checker('[{()]')
    False
    '''
1   s = []
1   balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
#n   for index in range(len(symbol_string)):
    1   symbol = symbol_string[index]
    1   if symbol in "([{":
    1       s.append(symbol)
    1   else:
    1       # if len(s)==0:
    1       if s==[]:
    1           balanced = False
    1       else:
    1           top = s.pop()
    1           if not matches(top,symbol):
    1               balanced = False
        index = index + 1
1   if balanced and s==[]:
1       return True
1   else:
1       return False


def _matches(left, right):
    lefts = "([{"
    rights = ")]}"
    return lefts.index(left) == rights.index(right)
