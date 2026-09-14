# stacks + intro to runtime analysis

<center>
<img width=60% src=tests2.jpg />
</center>

**Monday 14 Sep:**

1. Canvas grades up to date
    1. Still a few unsubmitted assignments

        You have until Friday this week to submit without penalty.
    1. Average topic00 quiz grade: 3.5/4

1. Error in homework test cases
    1. <https://github.com/mikeizbicki/cmc-csci046/issues/580>
    1. Late penalty applies for tomorrow's homework

1. Quiz this Wednesday
    1. "review" quiz: <https://github.com/mikeizbicki/quiz/blob/master/quiz_python_with_exceptions/topic06_oop.pdf>
    1. You are responsible for knowing the following exceptions
        1. `AssertionError`
        1. `AttributeError`
        1. `IndexError`
        1. `KeyError`
        1. `NameError`
        1. `UnboundLocalError`
        1. `TypeError`
        1. `ZeroDivisionError`

<!--
<img src=merge-conflict.jpg width=400px />
-->

<!--
For today's lecture:

1. You'll need to get the `stack.py` file to follow along with lecture

    1. Redo the `git pull` procedure from last week's lab

       > **HINT:**
       > If your `git pull` command tries to do a rebase instead of a merge, then add the `--rebase=false` command line parameter to get
       > ```
       > $ git pull upstream 2023spring --rebase=false
       > ```

Git notes:

1. Git is hard

1. We won't be going over new git material for a long time :)

1. Expect a git review problem on the quiz

    1. If you don't feel 100% confident with the git terminal commands, you should review the git lab from topic00

1. If you ever get *really* stuck, you can always delete your fork/clone and refork/reclone from scratch.
-->

## Lecture Notes

1. optional references:
    1. <https://www.geeksforgeeks.org/python/stack-in-python/>
    1. data structures textbook chapter 4: <https://runestone.academy/runestone/books/published/pythonds/BasicDS/toctree.html>

1. vocabulary
    1. abstract data types (ADTs)
        1. defines an interface
        1. no implementation details
    1. data structure
        1. defines an interface
        1. includes implementation details
    1. informally, ADTs are sometimes called data structures

1. stack ADT

    <img src=stack.webp width=800px />

    1. interface:
        1. `push`: add something to the top
        1. `pop`: take something off the top

    1. implementation:
        1. in Python, use a list to represent the stack ADT
        1. interface:
            1. `push` implemented with `append` method
            1. `pop` implemented with `pop` method

    1. balanced parenthesis algorithm
        1. key technical interview / leetcode question

## Lab

TBA
<!--
See the instructions in the [pytest-lab repo](https://github.com/mikeizbicki/pytest-lab).

1. pytest library
    1. Install with the command:
       ```
       $ pip3 install pytest
       ```
    1. Run all tests in the file `tests/test_main.py` with:
       ```
       $ python3 -m pytest tests/test_main.py
       ```
    1. If you don't include a filename, pytest will test all the files.
       You should test your extra credit with the command
       ```
       $ python3 -m pytest
       ```
    1. If you use the `-x` flag, then pytest will stop after the first error.
       This is useful for development.
       If you want to skip a test case and stop after the second, use the argument `--maxfail 2`.
       The `-x` flag is a shortcut for `--maxfail 1`.

1. runtime analysis
    1. big O/Omega/Theta notation

**Pre-lecture work:**

1. print the `big-o.pdf` file 

1. There is no required lab for this week.
   Instead, you just focus on completing the homework assignment (which is worth 12 points this week).

1. (optional)
   Some of my former students at UCR put together two games for testing your git skills.
   The games have you executing git commands to advance to the next level.
   The links are:

   1. https://github.com/git-game/git-game
   1. https://github.com/git-game/git-game-v2

   You can earn +1 point of extra credit for each game that you complete.
   To claim the extra credit, send me an email telling me how the game ends.
   -->

## Homework

TBA
