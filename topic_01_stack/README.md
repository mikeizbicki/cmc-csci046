# stacks

<center>
<img width=300px src=img/tests2.jpg />
</center>

**Monday 14 Sep:**

1. Canvas grades up to date
    1. Still a few unsubmitted assignments

        You have until Friday this week to submit without penalty.
    1. Average topic00 quiz grade: 3.5/4

1. Error in homework test cases
    1. <https://github.com/mikeizbicki/cmc-csci046/issues/580>
    1. Because I made an error, I will adjust due date to +2 days (this Thursday at midnight)

1. "review" quiz this Wednesday
    1. exceptions:
        1. practice problems: <https://github.com/mikeizbicki/quiz/blob/master/quiz_python_with_exceptions/topic04_exceptions.pdf>
        1. You are responsible for knowing the following exceptions
            1. `AssertionError`
            1. `AttributeError`
            1. `IndexError`
            1. `KeyError`
            1. `NameError`
            1. `UnboundLocalError`
            1. `TypeError`
            1. `ZeroDivisionError`
        1. If you need to review these exceptions, you can use the CS40 lectures:
            1. exceptions part 1: <https://www.youtube.com/watch?v=EQw8v2yT2Wg&list=PLSNWQVdrBwoaVBou5Yq_lSpk7Z4nCjzbX&index=17&pp=iAQBsAgC>
            1. more exceptions: <https://www.youtube.com/watch?v=5idOdtQKO5Q&list=PLSNWQVdrBwoaVBou5Yq_lSpk7Z4nCjzbX&index=16&pp=iAQBsAgC>
            1. the python code from those videos is available at: <https://github.com/mikeizbicki/cmc-csci040/blob/2026spring/topic_04_Python_Exceptions/exceptions_quizreview.py>
    1. OOP + memory management:
        1. practice problems: <https://github.com/mikeizbicki/quiz/blob/master/quiz_python_with_exceptions/topic06_oop.pdf>
        1. CS40 review lecture at: <https://www.youtube.com/watch?v=zYvdnxWakRk&list=PLSNWQVdrBwoaVBou5Yq_lSpk7Z4nCjzbX&index=11&pp=iAQBsAgC>
        1. **most quiz questions will come from this topic**

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

    <img src=img/stack.webp width=800px />

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

**Prelab work:**

1. Your prelab work is designed to help you learn vim.

    <img src=img/vim.jpg width=400px />

    Using the [vim cheatsheet](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf):

    1. select 10 verbs and 10 motions
    1. write by each of these commands and what they do
    1. do your best to memorize these commands and incorporate them into your workflow

**Instructions:**

See <https://github.com/mikeizbicki/lab-open-source>.

## Homework

See <https://github.com/mikeizbicki/html_validator>
