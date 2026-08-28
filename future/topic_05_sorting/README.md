# week 05: more recursion + sorting

## Announcments

1. The sorting homework will be relatively easy.

1. Lots of people still using your tools very inefficiently.

   Spend some time this week to review vim and get a good workflow.

   **Remember:**

   1. Boredom and drudgery are evil
   1. Laziness is good

   <br/>

   <img width=600px src=gates.jpg />

   <br/>

   <img width=600px src=the-three-chief-virtues-of-a-programmer-are-laziness-impatience-and-hubris-larry-wall.jpg />

<br/>

**Wed (22 Feb):**

1. From last class:
    1. iterative substitution not important
    1. master theorem is important
    1. you'll get review of it in the lab this week

1. We're about 1 week ahead of schedule right now

## Lecture

1. Recursion runtime analysis with the [Master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))

<!--
1. best case vs worst case vs average case runtime

    1. these are different that O/Omega/Theta, but often confused
-->

1. Sorting

    1. Theorem: every comparison based sorting algorithm has worst case runtime $\Omega(n \log n)$

       See: <https://en.wikipedia.org/wiki/Comparison_sort#Number_of_comparisons_required_to_sort_a_list>

   1. Every good computer scientist has the following table memorized.
      The notation is typically expressed using O() instead of Theta notation, but Theta is more accurate.

      | algorithm         | best case run time | average case run time | worst case run time | auxiliary space complexity | notes |
      | ----------------- | ------------------ | --------------------- | ------------------- | -------------------------- | ----- | 
      | [selection sort](https://en.wikipedia.org/wiki/Selection_sort)    | Θ(n^2) | Θ(n^2) | Θ(n^2) | Θ(1) | never used |
      | [bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) | Θ(n) | Θ(n^2) | Θ(n^2) | Θ(1) | never used |
      | [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort) | Θ(n) | Θ(n^2) | Θ(n^2) | Θ(1) | great constant factor; combined with other algorithms to improve best case behavior |
      | \*[merge sort](https://en.wikipedia.org/wiki/Merge_sort) | Θ(n log n) | Θ(n log n) | Θ(n log n) | Θ(n) | simple, easy analysis |
      | \*[quick sort](https://en.wikipedia.org/wiki/Quicksort) | Θ(n) | Θ(n log n) | Θ(n^2) | Θ(log n) | the most widely implemented sorting algorithm; fast constant factor but more difficult to analyze theoretically |
      | [tim sort](https://en.wikipedia.org/wiki/Timsort)   | Θ(n) | Θ(n log n) | Θ(n log n) | Θ(n) | default sort in python; optimized constant factor for real world data |
      | [heap sort](https://en.wikipedia.org/wiki/Heapsort) | Θ(n log n) | Θ(n log n) | Θ(n log n) | Θ(1) | we will implement a version later in the semester |
      | [radix sort](https://en.wikipedia.org/wiki/Radix_sort) | Θ(n) | Θ(n) | Θ(n) | Θ(n) | not a comparison based sort; only works for integers |

      Joke algorithm: [quantum bogo sort](https://quantumcomputing.stackexchange.com/questions/1265/what-can-we-learn-from-quantum-bogosort) runs in time O(1) but almost certainly destroys the universe

      **Shell sort**:
        1. interesting from a CS theory standpoint, but not from a practical standpoint
        1. the worst-case runtime is currently unknown
        1. researchers have bounded the runtime as

           <img src='shell_omega.svg' /><br/>

           <img src='shell_o.svg' />
        1. for details, see: <https://en.wikipedia.org/wiki/Shellsort>


   1. reference: [textbook sections 6.6-6.12](https://runestone.academy/runestone/books/published/pythonds/SortSearch/toctree.html)

**Fun:**

Since sorting is so fundamental to CS, it is one of the most popular source of comics.

From SMBC:

<img src=20121221.gif width=400px />

<br/>

<img src=1612627667-20210206.png width=400px />

<br/>

<img src=1611767129-20210127.png width=400px />

From XKCD:

<img src=ineffective_sorts_2x.png width=400px />

## Lab

See the instructions at <https://gitlab.com/mikeizbicki/master-theorem/>.

<!--
Use the master theorem to solve the following recurrence relations in Theta notation.

| recurrence           | solution                       | practical application                     |
| -------------------- | ------------------------------ | ----------------------------------------- |
| T(n) = T(n/2) + n    | Theta( n            ) | runtime of the bad binary search          |
| T(n) = T(n/2) + 1    | Theta( log n        ) | runtime of the correct binary search      |
| T(n) = T(n/3) + 1    | Theta( log n        ) | runtime of "trinary search"               |
| T(n) = 2T(n/2) + 1   | Theta( n            ) | runtime for [finding the median of an unsorted list](https://en.wikipedia.org/wiki/Quickselect) |
| T(n) = 2T(n/2) + n   | Theta( n log n      ) | runtime of merge sort                     |
| T(n) = 3T(n/3) + n   | Theta( n log n      ) | runtime of a trinary merge sort           |
| T(n) = T(n/2) + n^2  | Theta( n^2          ) |                                           |
| T(n) = 2T(n/2) + n^2 | Theta( n^2          ) |                                           |
| T(n) = 3T(n/2) + n^2 | Theta( n^2          ) |                                           |
| T(n) = 3T(n/2) + n   | Theta( n^(log_2 3)  ) | runtime of [Karatsuba's integer multiplication algorithm](https://en.wikipedia.org/wiki/Karatsuba_algorithm); HINT: Case 1 |
| T(n) = 7T(n/2) + n^2 | Theta( n^(log_2 7)  ) | runtime of [Strassen's matrix multiplication algorithm](https://en.wikipedia.org/wiki/Strassen_algorithm) |

**Submission:**
The answers are included as comments in the `README.md` file.
Check your answers for correctness,
and when you have finished,
submit a statement to sakai that you have completed the lab.
The lab will be graded for completion, not for correctness.

On your final, you will have multiple problems where you have to solve these recurrences.
-->
