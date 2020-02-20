from copy import copy, deepcopy
xs = [[1,2,3],[4,5,6]]
ys = copy(xs)

# main takeaway:
# probably should use deepcopy to copy

# common ways to do assigning
# 50%: =
# 49%: deepcopy
# 1%:  copy

# copy: only copies the list itself
# deepcopy: copies the list and everything
#           inside the list

#import copy
#zs = copy.copy(xs)
#from copy import copy
#zs = copy(xs)

xs[0][0]='hello'
#xs[0]='hello'

# can I access the original value of xs
# before the modifications?
# yes <- honest answer; HUGE RED FLAG; brittle
# no  <- what you should actually think

print('xs=',xs)
print('ys=',ys)

print('id(xs)',id(xs))
print('id(ys)',id(ys))

print('id(xs[0])',id(xs[0]))
print('id(ys[0])',id(ys[0]))
