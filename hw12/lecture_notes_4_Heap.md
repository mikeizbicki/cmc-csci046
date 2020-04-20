# Heaps

Heaps are binary trees,
but unlike BSTs and AVL Trees,
Heaps do not obey the binary search tree property.
Instead, the obey the "min-heap" property:
the value of a parent must be less than or equal to the children.
Heaps are also sometimes called priority queues.

This table summarizes the differences between the three binary tree structures runtimes:

|               | `insert`  | `find`    | `find_smallest`   | `remove`  | `remove_min`  | 
| ------------- |  -------- | --------- | ----------------- | --------- | ------------- |
| BST (worst)   | ϴ(n)      | ϴ(n)      | ϴ(n)              | ϴ(n)      | ϴ(n)          |  
| BST (ave)     | ϴ(log n)  | ϴ(log n)  | ϴ(log n)          | ϴ(log n)  | ϴ(log n)      |  
| AVLTree       | ϴ(log n)  | ϴ(log n)  | ϴ(log n)          | ϴ(log n)  | ϴ(log n)      |  
| Heap          | ϴ(log n)  | ---       | ϴ(1)              | ---       | ϴ(1)          |  

Heaps can be implemented in two ways:
1. using an array
1. using a binary tree
We will be using the binary tree method,
but the book (and many online resources) use the array method.

There are many variations of the heap data structure,
but the [fibonacci heap](https://en.wikipedia.org/wiki/Fibonacci_heap) is the most famous.
This is also the classic example of a "graduate level" data structure.

## Videos

**Essential:** The following series of videos by Rob Edwards explains the BST operations:
1. [Intro to heaps](https://www.youtube.com/watch?v=BzQGPA_v-vc&list=PLpPXw4zFa0uKKhaSz87IowJnOTzh9tiBk&index=44)
1. [Adding and removing](https://www.youtube.com/watch?v=7KhYwHfx40U&list=PLpPXw4zFa0uKKhaSz87IowJnOTzh9tiBk&index=45)
1. [This stackoverflow post](https://stackoverflow.com/questions/18241192/implement-heap-using-a-binary-tree) has some good hints on implementing a heap as a binary tree.

Questions:
1. You should be able to define a [*complete tree*](http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/FullvsComplete.html).
1. Given a picture of a Heap, you should be able to draw the result of an insertion and delection.
1. What is the maximum height of an Heap tree with n nodes?

