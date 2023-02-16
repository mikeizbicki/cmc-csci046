# Week 10: Binary Search Trees (BSTs) / Recursive Data Structures

<img width=600px src=cgxof0jkru551.png />

<!--
<img src=l5nus3752l261.png />
-->

1. Motivation:
    1. Binary search lets us check whether an element is in a sorted list in O(log n) time,
       but adding new elements to the sorted list takes O(n) time.

    1. Binary search trees (BSTs) let us perform both insertion and deletion in O(log n) time.

        1. The "right" way to think of them is as a combination of sorting and binary search algorithms merged together in one.
    
        1. Technically, the BST doesn't guarantee worst case runtimes of O(log n) time.

        1. It guarantees that the works case runtimes are O(height), and the height is O(n) in the worst case.

        1. Next week, we will extend the BST to the AVL tree, which guarantees the height is O(log n).

    1. The downside of BSTs is that their implementations will get very complicated.
       Fortunately, they only need to be implemented once, then everyone else can use them.

1. Reference:
    1. [Textbook](https://runestone.academy/runestone/books/published/pythonds/index.html) Sections 7.1-7.7, 7.11-1.14

1. Recursive data structures
    1. We won't cover:
        1. [singly linked lists](https://www.youtube.com/watch?v=FSsriWQ0qYE&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=5)
        1. [circular linked lists](https://www.youtube.com/watch?v=5WoNhm7sOnA&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=19)
        1. [doubly linked lists](https://www.youtube.com/watch?v=8kptHdreaTA&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=24)
    1. We will cover:
        1. binary trees
        1. binary search trees
        1. AVL trees
        1. Heap trees

1. 3 algorithms on binary trees:
    1. traversals
        1. pre-order
        1. in-order
        1. post-order
    1. height
    1. size

1. 3 algorithms on binary search trees:
    1. find
    2. insert
    3. delete

1. python concepts
    1. static methods
    1. superclasses, inheritance
    1. WET vs DRY programming
        1. WET: wastes everyone's time / we enjoy typing
        1. DRY: don't repeat yourself

           <img src=keep-my-diaper-and-my-code-dry.jpg />

## Lab

No separate graded lab.

## Homework instructions

1. The https://github.com/mikeizbicki/containers repo has a new branch called `unicode`.
   This branch contains the homework for this week.

1. You should:

    1. Create and checkout a branch in your homework repo called `bst`.
       `bst` should be based off of the `master` branch and not the `unicode` branch.

       **IMPORTANT:**
       If your `bst` branch is based off of your `unicode` branch instead of `master`,
       you will receive -2 points on the assignment.

    1. Pull the contents of my `bst` branch into your branch.

    1. Fix the file `containers/BinaryTree.py` and `containers/BST.py` so that all the test cases pass.

    1. Update your `README.md` file to include build status icons for both files.

    1. **IMPORTANT:**
       All your work must be done in the `bst` branch,
       and **you must not merge your work into either the `master` or `unicode` branches**.
       If you merge your work into either `master` or `unicode`, you will receive -2 points on the assignment.

1. Submit the link to your `bst` branch on github to sakai.
   If you submit a link to any other branch instead, you will receive -2 points on the assignment.
