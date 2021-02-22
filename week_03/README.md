# week 03: queues + more runtime analysis

<center>
<img width=40% src=tests.png />
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

1. [Click here to complete the mid-semester survey if you haven't already](https://docs.google.com/forms/d/1vJ9UnXJVtI9kxI3uobiB3TEh9EuLzfPR2SG4VRod-fU/)

1. Check your answers for page 9 of the `big-o.pdf` notes.
   (There is nothing to submit for this problem, it is only for your own reference.)
    1. `1 = O(n)`
    1. `2n log(n) = O(n^2)`
    1. `1 = Omega(1/n)`
    1. `log_2 n = Theta(log_3 n)`
    1. `log n = Omega(1/log n)`
    1. `5x10^30 = O(log n)`
    1. `log n = Theta(log n^2)`
    1. `2^n = O(3^n)`
    1. `1/n = O(sqrt(1/n))`
    1. `log n = O( (log n)^2 )`

1. The file `palindrome.py` contains two functions.
   Both functions check whether the input container is a palindrome,
   and both functions work correctly no matter whether the input container is a `str`, `list`, or `deque`.

   Run the doctests to verify that both functions are correct:
   ```
   $ python3 -m doctest palindrome.py
   ```

   Complete the following table, where each entry is the runtime of the corresponding function when the input `container` is of the corresponding type.
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

1. In this problem, you will use the [timeit module](https://docs.python.org/3/library/timeit.html) in python to actually calculate the runtimes of these two functions.
   This module is used on the command line in the following way:
   ```
   $ python3 -m timeit -s 'SETUP_CODE' 'CODE_TO_TIME'
   ```
   where `SETUP_CODE` is a code snippet that defines some variables, and `CODE_TO_TIME` is a code snippet that will get run 1000000 times in order to determine how fast the code is.

   For example, in order to measure the runtime of the `check_palindrome_1` function on a list and deque of length 5, we could run the commands:
   ```
   $ python3 -m timeit -s 'import palindrome; xs=[1,2,3,2,1]' 'palindrome.check_palindrome_1(xs)'
   $ python3 -m timeit -s 'import palindrome; from collections import deque; xs=deque([1,2,3,2,1])' 'palindrome.check_palindrome_1(xs)'
   ```
   Because these containers are so small, the runtime is insignificant.
   (I get about 0.7 microseconds for both examples).
   Neither of these functions is slow because `n` is small.

   What we're really interested in, however, is when `n` is large.
   We can easily generate large containers using python's container multiplication operator.
   For example `[1]*100000` will give us a container of length one hundred thousand with all ones.
   ```
   $ python3 -m timeit -s 'import palindrome; from collections import deque; xs=deque([1]*100000)' 'palindrome.check_palindrome_1(xs)'
   ```

   Complete the following table with actual measured runtimes by substituting the values for `xs` and the function in the command above.

   |                        | `xs=("1"*100000)` | `xs=([1]*100000)` | `xs=deque([1]*100000)` |
   | ---------------------- | ---------------- | ---------------- | --------------------- |
   | `check_palindrome_1`   |                  |                  |                       |
   | `check_palindrome_2`   |                  |                  |                       |

   You should observe that one of these entries is significantly slower than the others.
   This slow entry should match the asymptotically large entry from the previous problem.

**Submission:**
Copy/paste the completed tables into sakai.
Each table is worth 1 point.
