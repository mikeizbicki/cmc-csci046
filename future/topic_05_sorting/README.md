# week 05: recursion + sorting

<center>
<img src=1612627667-20210206.png width=400px />
</center>

Other sorting comics:
1. https://www.smbc-comics.com/comic/understanding-2
1. https://www.smbc-comics.com/comic/2012-12-21
1. https://www.smbc-comics.com/comic/2010-09-03
1. https://xkcd.com/1185/

## Lecture

1. Recursion

    1. continue analysis with the master theorem

1. best case vs worst case vs average case runtime

    1. these are different that O/Omega/Theta, but often confused

1. Sorting

    1. Theorem: every comparison based sorting algorithm has worst case runtime Omega(n log n)

       See: https://en.wikipedia.org/wiki/Comparison_sort#Number_of_comparisons_required_to_sort_a_list

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
        1. for details, see: https://en.wikipedia.org/wiki/Shellsort

   1. reference: [textbook sections 6.6-6.12](https://runestone.academy/runestone/books/published/pythonds/SortSearch/toctree.html)

## Lab

Use the master theorem to solve the following recurrence relations in Theta notation.

| recurrence           | solution                       | practical application                     |
| -------------------- | ------------------------------ | ----------------------------------------- |
| T(n) = T(n/2) + n    | <!-- Theta( n            ) --> | runtime of the bad binary search          |
| T(n) = T(n/2) + 1    | <!-- Theta( log n        ) --> | runtime of the correct binary search      |
| T(n) = T(n/3) + 1    | <!-- Theta( log n        ) --> | runtime of "trinary search"               |
| T(n) = 2T(n/2) + 1   | <!-- Theta( n            ) --> | runtime for [finding the median of an unsorted list](https://en.wikipedia.org/wiki/Quickselect) |
| T(n) = 2T(n/2) + n   | <!-- Theta( n log n      ) --> | runtime of merge sort                     |
| T(n) = 3T(n/3) + n   | <!-- Theta( n log n      ) --> | runtime of a trinary merge sort           |
| T(n) = T(n/2) + n^2  | <!-- Theta( n^2          ) --> |                                           |
| T(n) = 2T(n/2) + n^2 | <!-- Theta( n^2          ) --> |                                           |
| T(n) = 3T(n/2) + n^2 | <!-- Theta( n^2          ) --> |                                           |
| T(n) = 3T(n/2) + n   | <!-- Theta( n^(log_2 3)  ) --> | runtime of [Karatsuba's integer multiplication algorithm](https://en.wikipedia.org/wiki/Karatsuba_algorithm); HINT: Case 1 |
| T(n) = 7T(n/2) + n^2 | <!-- Theta( n^(log_2 7)  ) --> | runtime of [Strassen's matrix multiplication algorithm](https://en.wikipedia.org/wiki/Strassen_algorithm) |

**Submission:**
The answers are included as comments in the `README.md` file.
Check your answers for correctness,
and when you have finished,
submit a statement to sakai that you have completed the lab.
The lab will be graded for completion, not for correctness.

On your final, you will have multiple problems where you have to solve these recurrences.
