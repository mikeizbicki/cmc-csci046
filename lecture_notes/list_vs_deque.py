from collections import deque

# difference between lists vs deques
# is only runtimes of operations

# lists = stacks
xs = [1,2,3,4,5]

# O(1)
xs.append('a')
xs.append('b')
xs.append('c')

# O(n)
xs.insert(0,'d')
xs.insert(0,'e')
xs.insert(0,'f')

# indexing is O(1)
print('xs[4]=',xs[4])

print('xs=',xs)

# deques = queues
ys = deque([1,2,3,4,5])

# O(1)
ys.append('a')
ys.append('b')
ys.append('c')

# O(1)
ys.appendleft('d')
ys.appendleft('e')
ys.appendleft('f')

# indexing takes time O(n)
print('ys[4]=',ys[4])

print('ys=',ys)

print('ys.pop()=',ys.pop()) # O(1)
print('ys.pop()=',ys.pop())
print('ys.pop()=',ys.pop())
print('ys.pop()=',ys.pop())
print('ys.popleft()=',ys.popleft()) # O(1)
print('ys.popleft()=',ys.popleft())
print('ys.popleft()=',ys.popleft())
print('ys.popleft()=',ys.popleft())

print('xs.pop()=',xs.pop()) # O(1)
print('xs.pop()=',xs.pop())
print('xs.pop()=',xs.pop())
print('xs.pop()=',xs.pop())
print('xs.pop(0)=',xs.pop(0)) # O(n)
print('xs.pop(0)=',xs.pop(0))
print('xs.pop(0)=',xs.pop(0))
print('xs.pop(0)=',xs.pop(0))
