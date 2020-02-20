xs = [1,2,3,4,5]
ys = xs # assignment by reference
# ys and xs have the same id
# therefore, they have the same value
# every id has a unique value
# but every value can have multiple ids

ys[0] = 'hello'
xs[1] = 'world'

print('xs=',xs)
print('ys=',ys)

print('id(xs)',id(xs))
print('id(ys)',id(ys))

# modified ys, and xs also changed

# in python, when you say x = y
# creates a new variable x,
# sets the id of x to be the id of y

# each id is associated with a value
