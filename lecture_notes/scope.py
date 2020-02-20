x = 0
xs = [1,2,3,4,5]

if True:
    # suite
    # indentation block
    # variables defined within suite
    # can leave the suite
    # call them "global" variables
    x = 5
    x = 6
    y = 7

print('suite')
print('x=',x)
print('y=',y)
print('xs=',xs)

########################################
print('code block')

def foo():
    # not a suite; is a "code block"
    # variables defined within code block
    # cannot leave code block
    # these are "local" variables
    x = 3
    y = 3
    z = 3
    #xs = [1,2,3]
    xs[0] = 'hello world'
foo()

print('x=',x)
print('y=',y)
print('xs=',xs)
# this line causes a crash:
# print('z=',z)

########################################

print('code block example 2')

def baz():
    global x
    x = 3
    y = 3
    z = 3

def bar():
    global x
    x = 4

print('x=',x)
baz()
print('x=',x)
bar()
print('x=',x)
baz()

print('x=',x)
print('y=',y)

########################################

print('more experiments with containers')

xs = [1,2,3,4,5]
ys = [1,2,3,4,5]
zs = [1,2,3,4,5]
def fiz():
    # if a variable is defined within a
    # code block, it is local;
    # otherwise it is global
    xs = [1,2,3]
    zs[0] = 'hello'
    print('inside fiz, xs=',xs)
    print('inside fiz, ys=',ys)
    print('inside fiz, zs=',zs)
fiz()
print('xs=',xs)
print('ys=',ys)
print('zs=',zs)

########################################
print('multi function examples')

x = 0
def example_a():
    #global x
    x = 5

def example_b():
    x = 6

def example_c():
    example_a()
    example_b()

example_c()
print('x=',x)

########################################
print('deeper stack')

n=5
def function_a(n):
    print('function_a n=',n)

def function_b(n):
    print('function_b n=',n)
    # recursion(8)
    function_a(n-1)
    print('function_b n=',n)

def function_c(n):
    print('function_c n=',n)
    # recursion(9)
    function_b(n-1)
    print('function_c n=',n)

def function_d(n):
    print('function_d n=',n)
    # recursion(10)
    function_c(n-1)
    print('function_d n=',n)

#function_d(10)
function_a(10)
print('n=',n)


# DRY: don't repeat yourself

def recursion(n):
    if n==7:
        function_a(n)
    if n>7:
        print('recursion n=',n)
        recursion(n-1)
        print('recursion n=',n)

recursion(10)
