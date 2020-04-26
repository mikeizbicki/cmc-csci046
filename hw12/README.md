# Trees (3)

You will implement an extension to the binary tree called the heap.

**Due date:**
Tuesday, 28 April at midnight

**Learning Objectives:**

1. understand the heap data structure
1. understand a binary tree data structure that is not a binary search tree
1. more practice with object oriented programming
1. more practice with larger python projects 

## Tasks

This homework builds off of the `trees` repo for hw10.

1. Create a new branch `heap` based off of your `master` branch, and check it out.
    ```
    $ git checkout master
    $ git branch heap
    $ git checkout heap
    ```
    **NOTE:**
    It is important that your `heap` branch not contain any code for the `AVLTree` class,
    but that your repo continue have this code available in the `AVLTree` branch.
    If you do not meet these requirements, you will lose 5 points on your final submission.

    My version of the `trees` repo on github also has a `heap` branch.
    To see all remote branches, run the command
    ```
    $ git branch -r
    ```
    and you should see output that looks like
    ```
    upstream/avl
    upstream/heap
    upstream/master
    ```
    To incorporate the `upstream`'s `heap` branch into your own,
    issue the following pull request:
    ```
    $ git pull upstream heap
    ```

2. Edit the `Trees/Heap.py` file so that all the test cases pass.

3. Push your changes into the `heap` branch on github by running the command
    ```
    $ git push origin heap
    ```
    **DO NOT PUSH YOUR CHANGES TO THE `master` or `avl` BRANCH ON GITHUB,
    AND DO NOT MERGE YOUR CHANGES INTO YOUR LOCAL VERSION OF THESE BRANCHES.**

    Notice that the travis button will stay lit green,
    even if your test cases do not pass.
    This is because the travis button is following your `master` branch.
    You do not have to modify the `README.md` to point to your `heap` branch.

## Submission

Submit the link to the `heap` branch of your `trees` repo.

## Collaboration Policy

All forms of collaboration with other students are encouraged.
Please only look at another student's github repo if you are collaborating with them.
Remember that you are responsible for ensuring that you understand the material.
