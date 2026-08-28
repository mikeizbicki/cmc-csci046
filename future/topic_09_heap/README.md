# Heaps

<img src=tree.png />

Textbook Reference: [Chapters 7.8-7.10](https://runestone.academy/runestone/books/published/pythonds/Trees/PriorityQueueswithBinaryHeaps.html)

## Summary of Worst Case data structure runtimes


| data structure  | `insert`  | `insert_list` | `find`    | `find_smallest`   | `remove`  | `remove_min`  | 
| --------------- |  -------- | ------------- | --------- | ----------------- | --------- | ------------- |
| list (unsorted) | ϴ(1)      | ϴ(n log n)    | ϴ(n)      | ϴ(n)              | ϴ(n)      | ϴ(n)          |  
| list (sorted)   | ϴ(n)      | ϴ(n log n)    | ϴ(log n)  | ϴ(log n)          | ϴ(n)      | ϴ(n)          |  
| BST (ave)       | ϴ(log n)  | ϴ(n log n)    | ϴ(log n)  | ϴ(log n)          | ϴ(log n)  | ϴ(log n)      |  
| BST (worst)     | ϴ(n)      | ϴ(n^2)        | ϴ(n)      | ϴ(n)              | ϴ(n)      | ϴ(n)          |  
| AVLTree         | ϴ(log n)  | ϴ(n log n)    | ϴ(log n)  | ϴ(log n)          | ϴ(log n)  | ϴ(log n)      |  
| Heap            | ϴ(log n)  | ϴ(n log n)    | ---       | ϴ(1)              | ---       | ϴ(log n)      |  
| Fibonacci Heap  | ϴ(1)      | ϴ(n)          | ---       | ϴ(1)              | ---       | ϴ(log n)      |  

Note:
1. For a sorted list, bulk insert is equivalent to sorting a list; find element uses binary search
1. You should be able to construct examples that generate the best/worst case runtimes
1. We won't discuss the Fibonacci Heap implementation in class, but I want you to understand that the Heap we will discuss is not optimal

## Heap

1. A heap is a binary tree that is:

    1. Complete
       1. Every level except (possibly) the last level is full (i.e. every node has both a left and right child)
       1. The last level is filled in a left-to-right order

    1. Heap property:
        1. Min-heap: The value of any node is smaller than the value of its children
        1. Max-heap: The value of any node is larger than the value of its children

1. Operations:

   1. `insert`

   1. `remove_min`

   1. `find_smallest`

   1. (you should be annoyed that I've used `min` in some functions and `smallest` in others)

   1. pseudocode is provided in the comments of the `containers/Heap.py` file

<!--
## Hash-based data structures

1. our `AVLTree`/`BST` data structures implement the same interface as python's built-in `set`
    1. construct a set, removing duplicates
    1. check for containment

1. but the runtimes are different, see: https://wiki.python.org/moin/TimeComplexity
    1. python's built-in types use a hash table implementation, rather than a tree-based implementation
    1. in general, hash tables are "slightly" better in the average case, but MUCH worse in the worst case
        1. programming languages like C++ that really care about runtime use tree-based data structures
        1. lots of security vulnerabilities related to people using hash tables when they shouldn'y
            1. https://www.securityweek.com/hash-table-collision-attacks-could-trigger-ddos-massive-scale
            1. https://www.kb.cert.org/vuls/id/903934
    1. python uses hash-based data structures to provide an easier interface for beginners

1. a hash function converts a type into an integer (typically 64 bit)
   1. in python, implemented with the `__hash__` magic method
   1. good hashes are "random"
        1. they need to give the same number every time for the same input
        1. small changes in the input should result in large changes of the output

Advanced runtime analysis:
1. (not on final)
1. the runtimes of hash data structures are really the number of times we call the hash function

   the runtimes of tree data structures are really the number of times we call the `<`/`>` functions

   but what if those functions are particularly slow/fast?

    1. hash functions take time Theta(k) for inputs of size k
        1. very large constant factor (for a good hash)
    1. `<`,`>` operators used in tree-based methods take time O(1) in a typical case, and Theta(k) only in the worst case
        1. you can "early stop" the comparison as soon as you find the answer

1. overall "more correct" runtimes

    1. hash-set:
        1. insert/lookup/delete (ave): O(k)
        1. insert/lookup/delete (worst): O(n+k)
    1. avltree-set:
        1. insert/lookup/delete, average case comparisons, total runtime: O(log n)
        1. insert/lookup/delete, worst case comparisons, total runtime: O(k log n)
-->

## Homework

> **IMPORTANT:**
> You should think of this homework like a "take home test" with no time limit.
> Therefore, this homework has a modified collaboration policy:
> You may not work with another human on this assignment in any way.
> For example, you may not:
>     1. Discuss the code with another student.
>     2. Look at another student's code.
>     3. Visit the QCL for help with this assignment.
>     4. Post issues to github related to the assignment.
> If you do have a question, you can ask me in office hours or over email.
> I may or may not be able to answer your question.
> I will answer questions related to git or the heap at a high level, but I will not answer questions related to python.

1. Recall that git is a protocol, and not a webpage.
   This means that git can be used with many different websites, or no website at all.
   One popular alternative to GitHub is called GitLab, and your next homework assignment is hosted there.

   The repo located at <https://gitlab.com/mikeizbicki/random-project> contains a branch called `heap`.
   This repo is a fork of the <https://github.com/mikeizbicki/containers> repo;
   that means it contains all the same code, plus more.
   GitHub "forks" are a special type of fork where both versions of code are hosted on github,
   but in general a fork is any copy of a code repo.
   
   > **HISTORICAL NOTE:**
   > Linus Torvalds created git in 2005 to manage the Linux kernel source code.
   > (See detailed history [on wikipedia](https://en.wikipedia.org/wiki/Git#History).)
   > GitHub was founded 3 years later in 2008, and was definitely not the first website to host repos for open source software.
   > [SourceForge](https://en.wikipedia.org/wiki/SourceForge#History), for example, has been hosting SVN repos since 1999.
   > (SVN is an alternative VCS to git.)
   > "Fork" is a term that's been around in the open source community since the very beginning,
   > and is not something unique to GitHub.
   > Anytime you take someone else's open source code and modify it in any way, you've "forked" that code.
   > Typically, we reserve this word for when two projects share the same initial code,
   > but then do not merge each other's downstream commits for whatever reason.
   > See [wikipedia](https://en.wikipedia.org/wiki/Fork_(software_development)) for details.
   > 
   > Recall that Microsoft was viewed as the "evil tech giant" by the open source world in the 90s and 00s
   > because they used shady legal tactics to suppress open source software.
   > Today's tech giants like Google/Facebook are better at supporting open source software,
   > but they still do not support open standards (see Google's [AMP](https://www.eff.org/deeplinks/2020/07/googles-amp-canonical-web-and-importance-web-standards-0) and [Floc](https://www.eff.org/deeplinks/2021/03/googles-floc-terrible-idea) systems, and Facebook's [internet.org](https://www.eff.org/deeplinks/2015/05/internetorg-not-neutral-not-secure-and-not-internet) and [lobbying efforts](https://www.eff.org/deeplinks/2021/03/facebooks-pitch-congress-section-230-me-not-thee) ).
   > This is the fundamental reason that many programmers view these tech giants as "evil" today.

   Microsoft purchased GitHub in 2018 as part of a long-standing plan to ingratiate itself with the open source community.
   As part of that plan, they offered unlimited use of GitHub Actions as a free service for any open source developer.
   That's why we're using GitHub Actions in this class instead of one of the other alternatives.
   Last year, however, we used Travis CI, and when GitHub Actions eventually becomes non-free,
   I'll switch the class over to using a different free service.
   The advantage of an open protocol system like git is there is no lock-in,
   so you can always switch to a better service easily.

1. You should:

    1. Add a new remote to your local repo on the lambda server that points to the gitlab repo.

    1. Create and checkout a branch in your homework repo called `heap`.
       `heap` should be based off of the `bst` branch and not the `master` or `avltree` branches.

        > **IMPORTANT:**
        > The code in your `heap` branch will require that you have access to your `BinaryTree` class,
        > and that `BinaryTree` passes all the test cases.
        > You do not need to have a working `BST` or `AVLTree` class for this assignment.

    1. Pull the contents of the gitlab repo's `heap` branch into your branch.

    1. Fix the file `containers/Heap.py` so that all the test cases pass.

    <!--
    1. Create a new file `.github/workflows/heap.yml` that runs the test cases for the `Heap` class.
       You should use the existing files in `.github/workflows` as an example,
       and modify them for the `Heap` class.

       **IMPORTANT:**
       If you do not create your `heap.yml` file correctly,
       github actions will not run your test cases for you.
       You will therefore get a 0 on the assignment since we will not be able to grade it.
    -->

    1. Update your `README.md` file to include a build status icon for the Heap.

    1. All your work must be done in the `heap` branch,
       and you must not merge your work into the `master`, `bst`, `avltree` branches.
       If you merge your work into any of these branches, you will receive a -8 point penalty on the assignment.

1. Submit the link to your `heap` branch on github to sakai.
   If you submit a link to any other branch instead,
   you will receive a -8 point penalty on the assignment.
