# Binary Search Trees (BSTs)

<img width=300px src=img/cgxof0jkru551.png />

**Announcements Wednesday 28 Oct:**
1. Math Teach today, 3:15-4:30pm at the red benches outside Adams
1. Ath dinner with Zachary Horvitz, who will be talking about “The Age of a Billion Answers: Promise and Peril in AI’s Rare Outputs” on Thursday October 29 at 6:30pm.  <https://www.cmc.edu/athenaeum/events/20261029>

## Lecture Notes

1. Motivation for BST:
    1. Binary search:
        1. check whether an element is in a sorted list in $O(\log n)$ time
        1. adding/deleting elements to the sorted list takes $O(n)$ time

    1. Binary search trees (BSTs) let us perform both insertion and deletion in $O(\log n)$ time in the "average case".

        1. The "right" way to think of them is as a combination of sorting and binary search algorithms merged together in one.

        1. Technically, the BST doesn't guarantee worst case runtimes of $O(\log n)$ time.

        1. It guarantees that the works case runtimes are $O(height)$, and the height is $O(n)$ in the worst case.

        1. Next week, we will extend the BST to the AVL tree, which guarantees the height is $O(\log n)$.

    1. The downside of BSTs is that their implementations will get very complicated.

       Fortunately, they only need to be implemented once, then everyone else can use them.

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

1. WET vs DRY programming
    1. WET: wastes everyone's time / we enjoy typing
    1. DRY: don't repeat yourself

        OOP / class inheritence is a tool for "keeping your code DRY"

        <img src=img/keep-my-diaper-and-my-code-dry.jpg width=300px />

1. Reference:
    1. [Textbook](https://runestone.academy/runestone/books/published/pythonds/index.html) Sections 7.1-7.7, 7.11-1.14

        The textbook has a working implementation of a binary search tree that you can base your implementation on.
        The main difference is that they are implementing a "Dictionary/Map" interface (i.e. associate keys with values),
        and we are implmementing a "set" interface (only check if keys are contained in the tree, without associating with a value).
        The set is a bit simpler because there are fewer values to keep track of.
        We are focusing on the set implementation mainly so you can't just "copy/paste" their solutions and have to reimplement everything from scratch.
        You can definitely use their implementation as a guide, however.

## Lab

TBA

## Homework instructions

<img src=img/l5nus3752l261.png width=300px />

1. Get the starter code by running
    ```
    $ mkdir hw-bst
    $ cd hw-bst
    $ git remote add upstream /home/usertest/proj/hw-bst
    $ git pull upstream bst
    ```
    Notice that:
    1. You will be working in the `bst` branch instead of the `master`/`main` branch.
        Names of branches are like variable names or file names---they mean nothing to the computer and are just human conventions.
    1. The upstream here is not located on the internet but on the lambda server in my account.

        All git commands that refer to "remote" locations (like `git remote` or `git clone`) take an arbitrary url as an argument.

        url = *uniform* resource locator, and a path is just a particular example of a url

1. Put your code on github by:
    1. Create a new github repo
    1. Run
        ```
        $ git remote add origin <url_to_your_repo>
        $ git push origin bst
        ```

1. Fix the code so that the test cases pass,
    then submit your repo url to canvas.

> **NOTE:**
> Your next two homeworks will build off of this assignment.
> You will not be able to complete them if you do not get full credit on this assignment.
> Also, for those two assignments only, we will have a modified collaboration policy where you are not allowed to collaborate in any way with other humans (classmates and QCL mentors included).
> You will still be able to see me in office hours with questions though if you'd like.

<!--
1. The <https://github.com/mikeizbicki/containers> repo has a new branch called `bst`.
   This branch contains the homework for this week.

1. You should:

    1. Create and checkout a branch in your homework repo called `bst`.

    1. Pull the contents of my `bst` branch into your branch.

        > **IMPORTANT:**
        > All of your work for this assignment must be contained in the `bst` branch of your repo,
        > and the `master` branch must remain unchanged.
        > If your master branch is modified in any way,
        > you will receive a -8 point penalty on this assignment.

    1. Fix the file `containers/BinaryTree.py` and `containers/BST.py` so that all the test cases pass.

1. Submit the link to your `bst` branch on github to sakai.
   If you submit a link to any other branch instead,
   you will receive a -4 point penalty on the assignment.
-->
