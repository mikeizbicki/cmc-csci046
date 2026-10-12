'''
This file introduces memory complexity and the `yield` keyword.
'''

def factorial(n):
    '''
    Return the factorial of n.

    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(10)
    3628800

    Computational complexity: Theta(n)
    '''
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def all_factorials_1(n):
    '''
    Return all the factorials from 1 up to n.

    >>> all_factorials_1(1)
    [1]
    >>> all_factorials_1(2)
    [1, 2]
    >>> all_factorials_1(3)
    [1, 2, 6]
    >>> all_factorials_1(10)
    [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

    Computational complexity: Theta(n^2)
    '''
    ret = []
    for i in range(1, n+1):
        ret.append(factorial(i))
    return ret


'''
NOTE:

This function has only a single for loop,
so at first glance it looks like it has a linear runtime.
But the inner call to `factorial` results in a quadratic runtime.
We call this *accidentally quadratic*.

Accidentally quadratic functions happen all the time.
For a huge list, see: <https://accidentallyquadratic.tumblr.com/>.
'''


def all_factorials_2(n):
    '''
    Return all the factorials from 1 up to n.

    >>> all_factorials_2(1)
    [1]
    >>> all_factorials_2(2)
    [1, 2]
    >>> all_factorials_2(3)
    [1, 2, 6]
    >>> all_factorials_2(10)
    [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

    Computational complexity: Theta(n)
    '''
    result = 1
    ret = []
    for i in range(1, n+1):
        result *= i
        ret.append(result)
    return ret


'''
NOTE:

The following code will fail with a `MemoryError` exception.

>>> all_factorials_2(10000000000)

This is because we are allocating a very large list inside the function.
The size of this list is Theta(n),
and so we say that the *memory usage* of the function is Theta(n).

It's also ugly because we're not reusing any of our previous code,
and the rewritten code has to keep track of extra information.

KEY IDEA:

If we're only planning on looping over the results,
we don't actually need to create the entire list before looping.
We can create the elements one at a time.
'''


def all_factorials_3(n):
    '''
    Return all the factorials from 1 up to n.

    >>> list(all_factorials_3(1))
    [1]
    >>> list(all_factorials_3(2))
    [1, 2]
    >>> list(all_factorials_3(3))
    [1, 2, 6]
    >>> list(all_factorials_3(10))
    [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

    Computational complexity: Theta(n)
    Memory complexity: Theta(1)
    '''
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result


'''
NOTE:

The following code will not raise a `MemoryError`

>>> all_factorials_3(10000000000)

Functions that use the `yield` keyword are called generators in python.
The generator above is syntactic sugar for a class definition that implements the __iter__ dunder method.
The class below is an example.
'''

class Factorial:
    '''
    An iterable that contains all factorial numbers.

    >>> list(Factorial(1))
    [1]
    >>> list(Factorial(2))
    [1, 2]
    >>> list(Factorial(3))
    [1, 2, 6]
    >>> list(Factorial(10))
    [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    '''

    def __init__(self, n=None):
        '''
        n is the number of iterations we will run;
        if n is None, then we will run forever
        '''
        self.n = n

    def __repr__(self):
        return f'Factorial({self.n})'

    def __iter__(self):
        '''
        Every class that supports the __iter__ method is an "iterable".
        All iterables support for loops and can be converted into a list.
        '''
        return FactorialIter(self.n)


class FactorialIter:
    '''
    Store the information needed to iterate inside a for loop.
    All local variables in the generator function become attributes in this class,
    and parameters to the generator function are parameters to the iterator.
    '''

    def __init__(self, n):
        self.n = n
        self.result = 1
        self.i = 0

    def __next__(self):
        '''
        Return the "next" factorial number in our sequence.
        The factorial number corresponding to position self.i
        '''
        if self.i >= self.n:
            # we're at the end of the iteration
            # if we never raise StopIteration,
            # then the loop will go on forever
            raise StopIteration
        else:
            self.i += 1
            self.result *= self.i
            return self.result

