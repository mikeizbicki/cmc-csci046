# Binary Search Trees

Recall that binary search lets us check whether an element is in a sorted list in O(log n) time.
Adding new elements to the sorted list, however, takes O(n) time.
(If we add an element into the middle of the list, we must shift everything else over.)
Binary search trees solve this problem.
They let us perform both insertion and deletion in logarithmic time.

The material in these videos corresponds to [Section 7.1 - 7.7 and 7.11 - 7.14](https://runestone.academy/runestone/books/published/pythonds/Trees/toctree.html) in the textbook.
(We will cover the rest of chapter 7 in subsequent lectures.)


1. **Optional.** Linked lists.

    Linked lists are a simple type of data structure.
    In python, linked lists are never used directly,
    and so I'm not going to require that you implement them.
    (The `deque` data structure in the `collections` module is internally implemented with a doubly linked list,
    but the implementation is in C rather than Python.)
    Many programming interviews ask questions about linked lists.
    Some of the Binary Tree videos below mention linked lists,
    and so watching these videos may help you understand those videos a bit better.

    Videos:
    1. [Singly linked lists](https://www.youtube.com/watch?v=FSsriWQ0qYE&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=5)
    1. [Circular linked lists](https://www.youtube.com/watch?v=5WoNhm7sOnA&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=19)
    1. [Doubly linked lists](https://www.youtube.com/watch?v=8kptHdreaTA&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=24)

1. **Essential.** [Binary Trees in Python: Introduction and Traversal Algorithms](https://www.youtube.com/watch?v=6oL-0TdVy28&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=34)

    Notes:
    1. Notice that LucidProgramming is using *CamelCase* for classnames and *snake_case* for function/variable names.
       This is the standard convention in python,
       and you should follow this convention too.
    1. Notice that LucidProgramming is using vim as their text editor,
       but they use it slightly differently than I do:
        1. The first change is that they have only a single window open rather than two windows open.
           To execute their code, they use the [`:!` command](https://learnvimscriptthehardway.stevelosh.com/chapters/52.html#bang).
           This causes anything typed after the `:!` to be executed as if it were run in the terminal.
           Thus, typing `:!python3 binary_tree.py` runs the `binary_tree.py` file and displays the results.
        1. Their vim is configured very differently from mine.
           They use what's called [relative line numbers](https://jeffkreeftmeijer.com/vim-number/), and they have [autocompletion enabled](https://stackoverflow.com/questions/5169638/autocompletion-in-vim).
           In general, vim is highly customizable,
           and I strongly recommend you spend a few hours customizing vim to your liking.

    Questions:
    1. What are the definitions of *leaf*, *root*, *child*, *parent*, *grandparent*, *ancestor*, and *descendent* nodes?
    1. What is the *height* of a node/tree?
    1. What is the *level* of a node/tree?
    1. What is the procedure for a *preorder*, *inorder*, and *postorder* traversal of a binary tree?

1. **Optional.** Stacks/queues.

    Stacks and queues have an important relationship with tree traversal algorithms.
    These two videos show that relationship:

    1. [Level-order Traversal](https://www.youtube.com/watch?v=aM-oswPn19o&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=35)
    1. [Reverse level-order traversal](https://www.youtube.com/watch?v=bK6lijUbvms&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=36)

    Note that LucidProgramming creates explicit `Stack`/`Queue` classes inorder to emphasize the relationship between these abstract data types and the traversal algorithms,
    but that these classes should never be implemented in real python code.
    Recall that you should use the `[]` and `deque` types instead.

1. **Essential.** [Binary Trees in Python: Calculating the Height of Tree](https://www.youtube.com/watch?v=BDw8zzy3QiY&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=37)

    In your homework, you will have to implement functions that calculate the height of the tree,
    and this video provides code for doing that.

1. **Essential.** [Binary Trees in Python: Calculating the Size of Tree](https://www.youtube.com/watch?v=VbruT_rwfzQ&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=38)

    In your homework, you will have to implement functions that calculate the size of the tree,
    and this video provides code for doing that.

1. **Essential.** [Binary Search Tree Introduction - Insertion and Search](https://www.youtube.com/watch?v=yC83Kp2xig8&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=39)

    Notes:
    1. At timestamp 9:40, LucidProgramming talks about the time/space complexity operations of the BST.
       Notice that he uses big-O notation for both average and worst case performance.
       This is correct use of big-O notation.
       Some of the operations could be strengthened to use big-Theta notation,
       but most of the operations have an optimal big-Omega of Ω (1).

    Question:
    1. What is the runtimes for `insert`, `delete`, and `find` functions in the average and worst cases?
        What do the trees look like in each of these cases?
    1. What is the algorithm for the `find` and `insert` functions?
        You should understand these algorithms well enough that you can recite them from memory.


1. **Essential.** [Checking the BST Property](https://www.youtube.com/watch?v=sM4ebIEjRXo&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=40)

    Notes:
    1. LucidProgramming implements the `_inorder_print_tree` function in their `BST` class.
       This is a very WET (Wastes Everyone's Time / We Enjoy Typing) thing to do because we've already implemented this same exact function in the `BinaryTree` class.
       If we instead made `BinaryTree` a superclass of `BST`,
       we would get this function "for free".
       That is why in your homework assignment, `BST` is a subclass of `BinaryTree`.
    1. There is a major bug in the `_is_bst_satisfied` function.
        You will have to correct this bug in your implementation for the homework.

    Questions:
    1. What is the BST property?


1. **Essential.** [BSTs - insert and remove explained](https://www.youtube.com/watch?v=wcIRPqTR3Kc&t=201s)

    Notes:
    1. This video was made by [Colleen Lewis](http://blogs.hmc.edu/lewis/),
       one of the CS professors at Harvey Mudd.
    1. The most difficult homework problem will be to implement the `delete` function.
        I'm not giving you any code to get started with this problem,
        and you should be able to figure it out based on Colleen's explaination and the code you have for `find` and `insert`.

    Questions:
    1. What is the algorithm for the `delete` function?
        You should be able to reproduce this algorithm from memory.
