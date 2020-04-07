# AVL Trees

AVL trees are a special type of binary search tree.
They obey the normal BST invariant,
but they also obey a special AVL invariant that forces the tree to be balanced.
This guarantees that the find/insert/delete operations will take logarithmic time.
(Recall that BSTs had logarithmic runtime on average,
but linear runtime in the worst case.)

The material in these videos corresponds to [Section 7.15 - 7.17](https://runestone.academy/runestone/books/published/pythonds/Trees/toctree.html) in the textbook.

1. **Essential:** The following series of videos by Rob Edwards explains the BST operations:
1. [Rotations 1](https://www.youtube.com/watch?v=M0Y3kDuyUCU&list=PLpPXw4zFa0uKKhaSz87IowJnOTzh9tiBk&index=56)
1. [Rotations 2](https://www.youtube.com/watch?v=NczBLeco6XA&list=PLpPXw4zFa0uKKhaSz87IowJnOTzh9tiBk&index=57)
1. [The AVL Tree](https://www.youtube.com/watch?v=-9sHvAnLN_w&list=PLpPXw4zFa0uKKhaSz87IowJnOTzh9tiBk&index=59)
1. [Insertion into AVL Tree](https://www.youtube.com/watch?v=7m94k2Qhg68&list=PLpPXw4zFa0uKKhaSz87IowJnOTzh9tiBk&index=65)

    Questions:
    1. Given a picture of an AVL tree, you should be able to draw the result of applying the *left rotation* and a *right rotation* operations.
    1. What is the *balance factor*?
    1. What is the maximum height of an AVL tree with n nodes?
    1. Given a picture of an AVL tree, you should be able to draw the resulting tree after performing an insertion.
    1. You do NOT need to know how to perform a deletion in an AVL tree.  
    1. You should be able to draw an AVL tree such that the tree is no longer an AVL tree if you perform the ordinary binary search insertion/deletion operations.

1. **Optional:** [Mastering the vim language](https://www.youtube.com/watch?v=wlR5gYd6um0)

    This video shows some intermediate vim tricks that will make you much more productive in vim. 

<!--
Deletion notes: https://www.codesdope.com/course/data-structures-avl-trees/
-->

