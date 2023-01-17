'''
Implement a "data structure" that contains the numbers in the factorial function.
'''

# the yield keyword lets us simplify all of the stuff we did below into a simple function
def factorial(n):
    ret = 1
    for i in range(1,n+1):
        ret *= i
        yield ret
    # implicitly return None
    # yield XXXX is the return XXXX inside the __next__ function
    # raise StopIteration is equivalent to return None


# Factorial is the data strucutre that supports for loops;
# we know it supports for loops because it implements the __iter__ magic method
class Factorial:
    def __init__(self, n=None):
        '''
        n is the number of iterations we will run;
        if n is None, then we will run forever
        '''
        self.n = n

    def __iter__(self):
        return FactorialIter(self.n)


class FactorialIter: # this is the class that stores the information about a current iteration through the data structure
    def __init__(self, n):
        self.n = n
        self.ret = 1
        self.i = 0

    def __next__(self):
        '''
        The purpose of this function is to return the "next" factorial number in our sequence.
        The factorial number corresponding to position self.i
        '''
        if self.n is not None and self.n <= self.i:
            # raising an exception; exceptions can be called errors
            # "throw" instead of "raise"
            raise StopIteration
            # we're done, we should stop
            # if we never raise StopIteration,
            # then the loop will go on forever
        else:
            self.i += 1
            self.ret *= self.i
            return self.ret

#def next(x):
#    return x.__next__()

'''
for i in Factorial(10):
    print("i=",i)

'''
for i in Factorial():
    print("i=",i)
    if i>10000:
        break

# whenever there is a for loop in python;

tmp = Factorial().__iter__()
while True:
    i = tmp.__next__()
    print("i=",i)
    if i>10000:
        break


'''
xs = [1, 2, 3, 4, 5]
for x in xs:
    pass

xs.__iter__()  # this will return an iteration object
               # the iterable object must have the __next__ method defined within it
'''
