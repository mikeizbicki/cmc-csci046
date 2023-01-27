

# list function converts any *iterable* into a list

xs = [1, 2, 3]
for x in list(range(4)):
    #print(x)
    #print('x=',x)
    
    # vim macros
    print("x=",x)


# very common pattern, called the "filtering pattern"
xs = []
for i in range(10):
    if i%2==0:
        xs.append(i)
print("xs=",xs)


# filter is a function taking 2 parameters
# param1: is a function that returns True for inputs 
#         we should keep
# param2: is a list (or iterable) that we're filtering 
evens = list(filter(lambda x: x%2==0, range(0,10)))
print("evens=",evens)


# lambda creates an "anonymous function"
def is_even(x):
    return x%2==0

new_function = is_even

# I'm not calling the is_even function!!!
# We're passing the function,
# and not the result of the function.
# Passing functions into functions is called
# functional programming.
evens2 = list(filter(new_function, range(0,10)))
print("evens2=",evens2)

print('hello world')


def my_filter(f, old_xs):
    xs = []
    for i in old_xs:
        # item for this iteration = old_xs[i]
        if f(i):
            xs.append(i)
    return xs


evens2 = list(my_filter(new_function, range(5,10)))
print("evens2=",evens2)

'''
mapping pattern
'''
xs = []
for i in range(10):
    xs.append(i*i)
print("xs=",xs)

# map applies its first parameter to every entry
# every entry is included in map;
# only some entries are included in filter;
# map does computation and changes the values;
# filter does not change the values of the iterable
squares = list(map(lambda x: x*x, range(10)))
print("squares=",squares)


# a little unpythonic to use map/filter
# what is more pythonic is list comprehension
# syntactic sugar of map/filter functions
# syntactic sugar does not add new features to the lang
# it just makes it sweeter (nicer/more pleasant) to use
# python has lots of syntactic sugar
# good: once you know all the sugars
# bad: there's lots of sugars to learn

evens = [ x for x in range(10) if x%2==0 ] # filter, no map
squares = [x*x for x in range(10) ] # map, no filter

even_squares = [ x*x for x in range(10) if x%2==0 ]


# formal definition of list comprehension syntax:
# [ expression(item) for item in iterable if condition(item) ]



