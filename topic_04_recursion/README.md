# topic 04: recursion + more runtimes + binary search

<center>
<img src=r_154444_mWjbZ.jpg width=400px />

<br/>
<br/>

[GNU](https://en.wikipedia.org/wiki/GNU_Project) is the name of an open source project that replicates much of the UNIX operating system.
It is a recursive acronym standing for "GNU's Not UNIX".

<img src=Strip-Oracle-v-Google-650-finalenglish-4.jpg width=400px />
</center>

## Announcements

1. My solution to the HTML_Validator homework is posted at <https://github.com/mikeizbicki/html_validator/blob/solution/HTML_Validator.py>

1. Word ladder notes:
    1. Second hardest homework you'll have
    1. Next few homeworks will be easier (... but not easy ...)
    1. Most of your grade is in the projects
        1. Historically, most students are not able to solve all problems
        1. This is what will separate As/Bs/Cs in the class
        1. Word ladder is worth (very approximately) 5% of your final grade

## Lecture

1. Debugging tips
    1. Always verify helper functions first
    1. Run the tests in a separate terminal from vim
    1. Use vim to open multiple files at once
    1. Make full use of the pytest output
    1. Use `--last-failed` (skip successful tests) and `-x` (stop after first failed test)
    1. Test parts of code without using pytest (and do this often!!!)
    1. Run tests in parallel
       ```
       $ pip3 install pytest-xdist
       $ python3 -m pytest -n4
       ```
       My solution takes about 5 minutes to run with this command,
       and 8 minutes to run with the non-parallel command.

1. Search
    1. the most fundamental/important problem of computer science
    1. sequential search:
        1. works for any input
        1. worst case runtime is $\Theta(n)$
    1. binary search
        1. requires the input be sorted; we will see next week that this takes time $\Theta(n \log n)$
        1. worst case runtime is $\Theta(\log n)$ ---- this is really, really fast!!!
    1. Reference: [textbook chapter 6.1-6.4](https://runestone.academy/runestone/books/published/pythonds/SortSearch/toctree.html)

1. More runtime analysis

   Official python documentation for container runtimes: <https://wiki.python.org/moin/TimeComplexity>

   <img src=math.webp width=300px />

1. Recursion
    1. Closely related to proof by induction (CSCI055/MATH055: discrete math)
    1. Every algorithm can be written either
        1. iteratively (using loops)
        1. recursively (by calling itself)
        1. see examples in `notes.py`
    1. Three laws of recursion according to the textbook
        1. A recursive algorithm must have a base case.
        1. A recursive algorithm must change its state and move toward the base case.
        1. A recursive algorithm must call itself, recursively.
    1. If these laws are not satisfied, then a *stack overflow* occurs.
       This is the recursive analogue of an infinite loop.
    1. Advantage of recursion:
        1. Easy to prove that algorithms are correct (CSCI148: algorithms)
        1. Easy to prove the runtime of the algorithm using the [Master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
        1. Many algorithms that require while loops are much simpler with recursion (e.g. binary search)
    1. Disadvantage of recursion:
        1. for loops are easier when they are applicable
    1. Reference: [textbook chapter 5](https://runestone.academy/runestone/books/published/pythonds/Recursion/TheThreeLawsofRecursion.html)

## Lab

TBA (there will be required partner work)

<!--
The format of this lab is similar to last week's.
There are two tables for you to fill out and submit to sakai.

1. First, we will measure just how good the O(log n) runtime for binary search is.

   The following terminal command measures the runtime of the `binary_search_itr` function from the `notes.py` file on a list of length `n=100000`:
   ```
   $ python3 -m timeit \
        -s 'import notes; n = 100000; xs = list(range(-n,n))' \
        'notes.binary_search_itr(xs,5)'
   ```

   For each cell in the table below:
   Modify the command above for the corresponding search function and value of `n`;
   measure the runtime and enter it into the table.

   |                | `sequential_search_itr`   | `binary_search_itr`   |
   | -------------- | ------------------------- | --------------------- | 
   | `n=1`          |                           |                       |
   | `n=10`         |                           |                       |
   | `n=100`        |                           |                       |
   | `n=1000`       |                           |                       |
   | `n=10000`      |                           |                       |
   | `n=100000`     |                           |                       |
   | `n=1000000`    |                           |                       |
   | `n=10000000`   |                           |                       |

   In my experiments:
   1. I get that binary search with `n=10000000` is faster than sequential search with `n=100`.
   1. Multiplying `n` times 10 gives a *multiplicative( slowdown for sequential search (by a factor of 10),
      but an additive slowdown for binary search (by about 5usec).

      You should ensure that this multiplicative vs additive slowdown makes sense to you based on the properties of logarithms.

   At [FAANG](https://en.wikipedia.org/wiki/Big_Tech#FAANG)-type companies,
   they are searching through datasets of size `n>1000000000000000` (15+ zeros).
   It should hopefuly be clear from these examples that the logarithmic runtime is absolutely essential for any realtime queries of datasets of this size.

1. In this problem we will compare the runtime of binary search on four of python's container types: list, deque, tuple, and array.

   We've already covered the list/deque types extensively in class.
   The tuple type is one that you've also seen.
   In python,
   it's denoted using parentheses instead of square brackets.
   For example, the following two commands both define equivalent tuples:
   ```
   >>> xs = (1, 2, 3, 4, 5)
   >>> xs = tuple(range(1,6))
   ```
   Tuples can be indexed and sliced just like lists in python, but they are immutable.
   This means that they cannot be updated (for example with the `append` method),
   and are therefore slightly more efficient.
   
   The array type is likely one that you haven't seen before,
   since it is not usually introduced in intro programming courses.
   The array type is included in the numpy library.
   You create an array by first importing the library,
   and then calling the `array` constructor on an iterable (i.e. list-like container):
   ```
   >>> import numpy
   >>> numpy.array([1, 2, 3, 4, 5])
   array([1, 2, 3, 4, 5])
   >>> numpy.array(range(1,6))
   array([1, 2, 3, 4, 5])
   ```
   The array supports a very similar interface as a list.
   For example, you can index and slice just like in a list:
   ```
   >>> xs = numpy.array(range(1,6))
   >>> xs[3]
   4
   >>> xs[3:]
   array([4, 5])
   ```
   The purpose of the array is to support numerical computations from linear algebra,
   and it behaves differently than lists with respect to the `+` and `*` operators.
   Lists use "container algebra" operations:
   ```
   >>> [1, 2] + [3, 4]
   [1, 2, 3, 4]
   >>> [1, 2]*2
   [1, 2, 1, 2]
   ```
   and arrays use "vector algebra" operations:
   ```
   >>> [1, 2] + [3, 4]
   [4, 6]
   >>> [1, 2]*2
   [2, 4]
   ```
   In this problem, the important difference will be that:
   1. list slices make a copy and take time O(k), where k is the size of the slice;
   1. array slices do not make a copy and take time O(1).
   To see that array slices do not make a copy,
   run the following sequence of commands:
   ```
   >>> xs = numpy.array([1, 2, 3, 4, 5])
   >>> xs
   array([1, 2, 3, 4, 5])
   >>> ys = xs[3:]
   >>> ys
   array([4, 5])
   >>> ys[0] = -1
   >>> ys[1] = -2
   >>> xs
   array([ 1,  2,  3, -1, -2])
   ```
   **NOTE:**
   If it's not obvious to you how these commands would generate different output if `xs` were a list,
   then you should also run them for `xs = [1, 2, 3, 4, 5]` before continuing.

   The following terminal command measures the runtime of the `binary_search_itr` command from the `notes.py` file on an array of length `n=100000`:
   ```
   $ python3 -m timeit \
        -s 'import notes; import numpy; n = 100000; xs = numpy.array(range(-n,n))' \
        'notes.binary_search_itr(xs,5)'
   ```

   For each cell in the table below:
   Modify the command above for the corresponding search function and container type;
   measure the runtime and enter it into the table.

   |                            | `array`  | `list`  | `tuple`     | `deque`       |
   | -------------------------- | ---------| --------|------------ | ------------- |
   | `sequential_search_itr`    |          |         |             |               |
   | `sequential_search_rec`    |  ---     | ---     |  ---        |  ---          |
   | `binary_search_itr`        |          |         |             |               |
   | `binary_search_rec`        |          |         |             |               |
   | `binary_search_rec2`       |          |         |             |  ---          |

   You should notice that:
   1. for the `array` container, all implementations of binary search work well
   1. for the `list` container, the binary search that relies on slicing is slow
   1. the `tuple` container behaves just like the list container
   1. binary search provides no speed up for the `deque` container;
      the `deque` container also does not support slicing, and so the `binary_search_rec2` function will have a type error
   1. the `sequential_search_rec` gets a `RecursionError` for large `n` values;
      this is one of the reasons we tend to prefer for loops over recursion when possible

   We will prove all of these statements formally next week in class by showing that the runtimes are:

   |                            | `array`  | `list`  | `tuple`     | `deque`       |
   | -------------------------- | ---------| --------|------------ | ------------- |
   | `sequential_search_itr`    | O(n)     | O(n)    | O(n)        | O(n)          |
   | `sequential_search_rec`    | ---      | ---     | ---         | ---           |
   | `binary_search_itr`        | O(log n) | O(log n)| O(log n)    | O(n)          |
   | `binary_search_rec`        | O(log n) | O(log n)| O(log n)    | O(n)          |
   | `binary_search_rec2`       | O(log n) | O(n)    | O(n)        | ---           |

To submit your lab, copy your completed tables with runtimes into sakai.
There is no need to copy the big-o table.

1. Recall that a python list is created with square brackets `[]` or the `list` function:
   ```
   >>> list1 = [1, 2, 3, 4, 5]
   >>> list2 = list(range(5))
   ```
   and a tuple is created with parentheses:
   ```
   >>> tuple1 = (1, 2, 3, 4, 5)
   >>> tuple2 = tuple(range(5))
   ```

   For both the list and the tuple, you can use the same syntax for indexing and slicing.
   In particular, you use square brackets for both a list and a tuple.
   ```
   >>> list1[3]
   4
   >>> list1[3:]
   [4, 5]
   >>> tuple1[3]
   4
   >>> tuple1[3:]
   (4, 5)
   ```

   The difference between lists and tuples is that lists are "mutable" (we can modify the container) and tuples are "immutable" (we cannot modify the container).
   The following code is okay:
   ```
   >>> list1[3] = 7
   >>> list1[3:] = [10, 11]
   ```
   The following code will generate errors:
   ```
   >>> tuple1[3] = 7
   >>> tuple1[3:] = (10, 11)
   ```
   Notice that it's perfectly okay to reassign the variable name that refers to a tuple:
   ```
   >>> tuple1 = (1, 2, 3)
   ```
   This doesn't modify original tuple, it creates an entirely new tuple in memory.
   That's why it's okay.

   The tuple type's immutability lets it perform certain indexing operations much faster.
   In particular, it is never necessary to copy a tuple,
   and so tuple slices take time O(1) instead of time O(k).

   Complete the following table with actual measured runtimes by substituting the values for `xs` and the function in the command above.

   |                        | `xs=("1"*100000)` | `xs=([1]*100000)` | `xs=deque([1]*100000)` |
   | ---------------------- | ---------------- | ---------------- | --------------------- |
   | `check_palindrome_1`   |                  |                  |                       |
   | `check_palindrome_2`   |                  |                  |                       |

   You should observe that one of these entries is significantly slower than the others.
   This slow entry should match the asymptotically large entry from the previous problem.
   -->
