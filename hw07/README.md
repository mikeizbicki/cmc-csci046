# Sorting

You will implement the merge and quick sort algorithms.

**Due date:**
Sunday, 29 March at midnight

**Learning Objectives:**

1. understand how merge sort and quicksort work
1. practice recursion
1. practice using property-based tests

## Tasks

Complete the following tasks:

1. Fork the [sorting repo](https://github.com/mikeizbicki/sorting) and enable travis
1. Update the `README.md` file so that the travis button points to your repo
1. Implement the `_merged`, `merge_sorted`, and `quick_sorted` functions so that all test cases in `tests/test_main.py` pass.
   You must implement `merge_sorted` and `quick_sorted` recursively.

Your grade will be the percentage of test cases that successfully pass in travis.

### Extra credit

The main advantage of quicksort is that it can be implemented using only Theta(1) memory,
whereas merge sort requires Theta(n) memory.
The downside of implementing quicksort in this way is that it will no longer be a [stable sort](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability).

If you implement the `quick_sort` function using only O(1) memory,
you will get 1 pt extra credit.
(The docstring for the function has instructions on how to do this.)
You must enable the extra travis test cases by uncommenting the extra credit line in `.travis.yml`.

## Submission

Submit the link to your forked repository on sakai.

If you completed the extra credit, write a note in sakai so that I know to grade it.

## Collaboration Policy

**You are not allowed to look at another student's github repo.**

All other forms of collaboration with other students are encouraged.
You may use any other online resources you like to complete this assignment.

