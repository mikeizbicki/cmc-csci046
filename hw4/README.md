# Word Ladders with Stacks and Queues

You will implement a solution to Lewis Carroll's [word ladder game](https://en.wikipedia.org/wiki/Word_ladder).

**Due date:**
Sunday, 23 February at midnight


**Learning Objectives:**

1. implement a complex algorithm involving both queues and stacks
1. understand python memory management
1. practice translating pseudocode into python
1. practice using the github/travis toolchain

## Background

A word ladder is a list of words where each word differs by only a single letter from the previous word.
For example, we can convert a `stone` into `money` using the following ladder:

```
stone
atone
alone
clone
clone
coons
conns
cones
coney
money
```

In this assignment, you will implement a function `word_ladder` that generates these word ladders.
There are many possible algorithms to generate word ladders, 
but a simple one uses a combination of stacks and queues as shown in the following pseudocode.

```
Create a stack
Push the start word onto the stack
Create a queue
Enqueue the stack onto the queue

While the queue is not empty
    Dequeue a stack from the queue
    For each word in the dictionary
        If the word is adjacent to the top of the stack
            If this word is the end word
                You are done!
                The front stack plus this word is your word ladder.
            Make a copy of the stack
            Push the found word onto the copy
            Enqueue the copy
            Delete word from the dictionary
```

This pseudocode is intentionally vague,
and I encourage you to ask clarifying questions.

## Tasks

Complete the following tasks:

1. Fork the [word\_ladder repo](https://github.com/mikeizbicki/word_ladder) and enable travis
1. Update the `README.md` file so that the travis button points to your repo
1. Implement the `word_ladder`, `verify_word_ladder`, and `_adjacent` functions so that all test cases in `tests/test_main.py` pass

Your grade will be the percentage of test cases that successfully pass in travis.

## Submission

Submit the link to your forked repository on sakai.

## Collaboration Policy

**You are not allowed to look at another student's github repo.**

All other forms of collaboration with other students are encouraged.
You may use any other online resources you like to complete this assignment.
