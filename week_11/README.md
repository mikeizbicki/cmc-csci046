# Week 11: AVL Trees

<img src=x9vlbv8frut01.jpg />

<br>
<br>

<img src=96irozk7ae761.jpg />

Textbook Reference: [Chapters 7.15-7.17](https://runestone.academy/runestone/books/published/pythonds/Trees/BalancedBinarySearchTrees.html)

## BST runtimes

The BST is "usually" good, but it can become "unbalanced", resulting in poor performance.

**Theorem:**
The runtime of find/insert/delete on any BST is O(height).

**Property:**
The height of any BST is O(n).

**Corollary:**
The runtime of find/insert/delete on any BST is O(n).

## Self-balancing BST

[Self-Balancing BSTs](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree) are a class of data structures that fix these problems

1. We will study the AVL Tree 

    1. invented in 1962 by Soviet scientists Adelson-Velsky and Landis
    1. particularly simple, and (I believe) historically the first

1. Other examples include

    1. 2-3 tree
    1. AA tree
    1. B-tree
    1. Red-black tree <-- invented in 1972 by West German Rudolf Bayer
    1. Scapegoat tree
    1. Splay tree
    1. Tango tree
    1. Treap
    1. Weight-balanced tree

1. All of these data structures add new invariants that somehow enforce that the tree be balanced

    1. The AVL invariant is particularly simple:

       The `balance_factor` of every node must be either -1, 0, or 1, where

       ```
       balance_factor = height(left subtree) - height(right subtree)
       ```

    1. **Theorem:**
       Every tree satisfying the AVL invariant has height O(log n).

       Proof in textbook chapter 17.16.

    1. **Corollary:**
       The find/insert/delete operations take time O(log n).

1. In your homework:

    1. The `AVLTree` class will be a subclass of `BST`,
       because every AVL tree is also a BST

       1. This gives us `find`/`__contains__` operations "for free"

    1. You will have to implement:
        1. checking the AVL invariant
        1. left/right rotations
        1. inserting into the tree

    1. You will not have to implement deleting from the tree

## Homework instructions

1. The https://github.com/mikeizbicki/containers repo has a new branch called `avltree`.
   This branch contains the homework for this week.

1. You should:

    1. Create and checkout a branch in your homework repo called `avltree`.
       `avltree` should be based off of the `bst` branch and not the `unicode` or `master` branches.

       **IMPORTANT:**
        The code in your `avltree` branch will require that you have access to your `BinaryTree` and `BST` classes.
        If you don't have those classes because you didn't base your `avltree` branch off of `bst`, the code won't work.

    1. Pull the contents of my `avltree` branch into your branch.

       **IMPORTANT:**
       My `avltree` branch contains modifications to both the `containers/BST.py` file and the `tests/test_BST.py` file.
       You will likely have a merge conflict on the former file (because we've both made changes to it) that you'll have to resolve;
       you shouldn't have a merge conflict on the latter file because you shouldn't have made any changes to the test cases.
       You will also see that your `BinaryTree` test cases continue to pass (green badge),
       but that the test cases for your `BST` are now failing (red badge).
       This is because I've added a new method `__eq__` to the `BST` class that you must implement, and it has corresponding test cases.

    1. Fix the file `containers/BST.py` and `containers/AVLTree.py` so that all the test cases pass.

    1. Update your `README.md` file to include build status icons for the AVLTree.

    1. **IMPORTANT:**
       All your work must be done in the `avltree` branch,
       and **you must not merge your work into the `master`, `bst`, or `unicode` branches**.
       If you merge your work into any of these branches, you will receive -2 points on the assignment.

1. Submit the link to your `avltree` branch on github to sakai.
   If you submit a link to any other branch instead,
   you will receive -2 points on the assignment.

1. **GRADING:**
   Because there are fewer test cases in this assignment, and the assignment is worth more points, each failing test case penalizes you -2 points instead of -1 point as in other assignments.
