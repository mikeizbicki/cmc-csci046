# topic 03: queues + more runtime analysis

<center>
<img width=600px src=tests.png />
</center>

Announcements:

1. Good job collaborating during lab time
1. Grades up-to-date in sakai
1. Lots of students still haven't submitted the first assignment 

    there's no late penalty
    
    but you're officially behind

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

<!--
1. more runtime analysis
    1. <https://wiki.python.org/moin/TimeComplexity>
    1. <img src=math.webp />
-->

## Lab

Posted at <https://github.com/mikeizbicki/lab-timit>.
<!--
1. Check your answers for page 9 of the `big-o.pdf` notes.
   (There is nothing to submit for this problem, it is only for your own reference.)
    1. `1 = O(n)`
    1. `3n log(n) = O(n^2)`
    1. `1 = Omega(1/n)`
    1. `log_2 n = Theta(log_3 n)`
    1. `log n = Omega(1/log n)`
    1. `5x10^30 = O(log n)`
    1. `log n = Theta(log n^2)`
    1. `2^n = O(3^n)`
    1. `1/n = O(sqrt(1/n))`
    1. `log n = O( (log n)^2 )`

1.   Complete the following table, where each entry is the runtime of the corresponding function when the input `container` is of the corresponding type.
   Write the runtimes in terms of `n=len(container)` using big-O notation.

   |                        | `str` | `list` | `deque` |
   | ---------------------- | ----- | ------ | ------- |
   | `check_palindrome_1`   |  O(n) |        |         |
   | `check_palindrome_2`   |       |        |         |

   **HINT:**
   The runtimes for indexing into a string are the same as those for indexing a list, which is O(1).
   The runtime for indexing into a deque is O(n).

   **HINT:**
   One of these entries should be asymptotically larger than the others.
-->
