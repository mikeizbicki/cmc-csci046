import copy

xs = [1,2,3,4,5]
#ys = []
#for x in xs:
#    ys.append(x)
ys = copy.copy(xs) # copy by value

from copy import copy
ys = copy(xs)

print('ys=',ys)
ys[0] = 'hello'
print('ys=',ys)
xs[1] = 'world'
print('ys=',ys)

print('xs=',xs)
print('ys=',ys)

print('id(xs)',id(xs))
print('id(ys)',id(ys))

# modified ys, and xs did not change

