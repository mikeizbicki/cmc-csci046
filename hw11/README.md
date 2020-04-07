# Trees (2)

You will implement an extension to the binary search tree called the AVL tree.

**Due date:**
Sunday, 12 April at midnight

**Learning Objectives:**

1. understand the AVL tree data structure
1. understand balancing operations on trees
1. more practice with object oriented programming
1. more practice with larger python projects 

## Tasks

This homework builds off of the `trees` repo for hw10.

1. Create a new branch called `avl` and check it out.
    ```
    $ git branch avl
    $ git checkout avl
    ```
    My version of the `trees` repo on github also has an `avl` branch.
    To see all remote branches, run the command
    ```
    $ git branch -r
    ```
    and you should see output that looks like
    ```
    origin/avl
    origin/master
    ```
    To incorporate the origin's `avl` branch into your own,
    issue the following pull request:
    ```
    $ git pull origin avl
    ```
    Notice that the last argument is `avl` above,
    whereas it is more common to use `master` as the last argument because we typically want to pull from the `master` branch.
    Whatever branch we use as the last argument is the branch we will pull from.

    Your local `avl` branch will now have 2 new files in it that didn't exist before,
    and one modified file.
    To verify that you received these files correctly,
    we will calculate the *diff* between the `avl` branch and `master`.
    A diff is simply a list of all the changes between any two commits of a git repo.
    Run the command
    ```
    $ git diff --name-only master
    ```
    and you should get output like
    ```
    .travis.yml
    Trees/AVLTree.py
    tests/test_AVLTree.py
    ```
    Note that if you omit the `--name-only` flag from the command above (i.e. you run the command `git diff avl master`),
    the git will list not just the files that were added,
    but the contents of those files as well.

2. Edit the `Trees/AVLTree.py` file so that all the test cases pass.

3. Push your changes into the `avl` branch on github by running the command
    ```
    $ git push origin avl
    ```
    **DO NOT PUSH YOUR CHANGES TO THE `master` BRANCH ON GITHUB,
    AND DO NOT MERGE YOUR CHANGES INTO YOUR LOCAL `master` BRANCH.**

    Notice that the travis button will stay lit green,
    even if your test cases do not pass.
    This is because the travis button is following your `master` branch.
    You do not have to modify the `README.md` to point to your `avl` branch.

## Submission

Submit the link to the `avl` branch of your `trees` repo.

## Collaboration Policy

All forms of collaboration with other students are encouraged.
Please only look at another student's github repo if you are collaborating with them.
Remember that you are responsible for ensuring that you understand the material.
