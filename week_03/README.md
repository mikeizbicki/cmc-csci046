# week 03: queues + more runtime analysis

<center>
<img width=60% src=tests.png />
</center>

## Lecture

1. queue ADT
    1. in python, always implemented using deques (pronounced "decks")
       ```
       from collections import deque
       ```
    1. interface:
        1. `enqueue`: add something to the **top**; in python, we use the `append` method; same as stacks/lists
        1. `dequeue`: take something off the **bottom**; in python, we use the `popleft` method; different from stacks/lists
    1. the differences between a stack and queue are summarized by
    
        1. stack = FILO (first in last out)

        1. queue = FIFO (first in first out)

        1. <a href=https://gohighbrow.com/stacks-and-queues/><img src=stack-v-queue.png /></a>

    1. Reference: [textbook chapter 4](https://runestone.academy/runestone/books/published/pythonds/BasicDS/toctree.html)

1. more runtime analysis
    1. continue big-o notes
    1. https://wiki.python.org/moin/TimeComplexity

## Lab

TBA

<!--
palindrome checker
-->
