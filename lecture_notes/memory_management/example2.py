xs = [1,2,3,4,5]
ys = [1,2,3,4,5]

# everytime we create a new list using []
# it creates a new id that "points" to value

ys[0] = 'hello'
xs[1] = 'world'

print('xs=',xs)
print('ys=',ys)

print('id(xs)',id(xs))
print('id(ys)',id(ys))

# modified ys, and xs did not change
