# Lab: timeit

## Submission details

Fork this repo and clone your fork on the lambda server.
The instructions below will ask you to directly edit the README file of your fork.
After you've made these edits,
upload your changes to github
and submit the url to sakai.

## Instructions

**Part 0:**

The file `palindrome.py` contains two functions.
Each function checks whether the input container is a palindrome,
and each function works correctly no matter whether the input container is a `str`, `list`, or `deque`.

Run the doctests to verify that all functions are correct:
```
$ python3 -m doctest palindrome.py
```
Now open the `palindrome.py` file in vim and verify that the doctests are testing all both functions using all three data types.
Read through the implementation of the functions,
and make sure you understand how they work.
Take a guess at which one will be faster,
and tell the person sitting next to you what your guess is.

<!--
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
-->

**Part 1:**

Now you will use the [timeit module](https://docs.python.org/3/library/timeit.html) in python to measure the runtimes of the palendrome functions.
This module is used in the terminal in the following way:
```
$ python3 -m timeit -s "$SETUP_CODE" "$CODE_TO_TIME"
```
where `$SETUP_CODE` is python code whose runtime we don't want to measure (but need to run to setup the problem),
and `$CODE_TO_TIME` is python code whose runtime we will measure.
The `$CODE_TO_TIME` will get run many times,
and `timeit` will report the average runtime.

For example, in order to measure the runtime of the `check_palindrome_1` function on a list and deque of length 5, we could run the commands:
```
$ CODE_TO_TIME='palindrome.check_palindrome_1(xs)'
$ python3 -m timeit -s 'import palindrome; xs=[1,2,3,2,1]' "$CODE_TO_TIME"
$ python3 -m timeit -s 'import palindrome; from collections import deque; xs=deque([1,2,3,2,1])' "$CODE_TO_TIME"
```
Because these containers are so small,
the runtimes are insignificant.
(I get about 0.7 microseconds for both examples).
It is common to use the letter $n$ to denote the length of a container.
With this notation, we can also say that because $n$ is small, the runtimes are insignificant.

What we're really interested in, however, is when $n$ is large.
We can easily generate large containers using python's container multiplication operator.
For example `[1]*65536` will give us a container of length one hundred thousand with all ones.
(65536 is $2**16$.  Since it is the largest number that can be stored in two bytes, it appears in many places.)
If you've never used python's container multiplication feature before,
open up an interactive python session and try it:
```
$ python3
>>> [1]*65536
```

Now time the `check_palindrome_1` function on a deque of that size:
```
$ python3 -m timeit -s 'import palindrome; from collections import deque; xs=deque([1]*65536)' 'palindrome.check_palindrome_1(xs)'
```

Complete the following table with actual measured runtimes by substituting the values for `xs` and the function in the command above.

|                        | `xs=("1"*65536)` | `xs=([1]*65536)` | `xs=deque([1]*65536)` |
| ---------------------- | ---------------- | ---------------- | --------------------- |
| `check_palindrome_1`   |                  |                  |                       |
| `check_palindrome_2`   |                  |                  |                       |

You should observe that one of these entries is significantly slower than the others.
This tells us that the runtime of a function depends on: (1) the algorithm that it is implemented with, and (2) the data types it is run on.

An good programmer can easily predict which combination above would be slow without running it,
and we'll cover in class next week how you can make this same prediction.
