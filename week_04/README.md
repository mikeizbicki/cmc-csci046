# week 04: recursion + binary search

<center>
<img src=r_154444_mWjbZ.jpg width=400px />

<br/>
<br/>

[GNU](https://en.wikipedia.org/wiki/GNU_Project) is the name of an open source project that replicates much of the UNIX operating system.
It is a recursive acronym standing for "GNU's Not UNIX".

<img src=Strip-Oracle-v-Google-650-finalenglish-4.jpg width=400px />
</center>

## Lecture

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

1. Search
    1. the most fundamental/important problem of computer science
    1. sequential search:
        1. works for any input
        1. worst case runtime is Theta(n)
    1. binary search
        1. requires the input be sorted; we will see next week that this takes time Theta(n log n)
        1. worst case runtime is Theta(log n)
    1. Reference: [textbook chapter 6.1-6.4](https://runestone.academy/runestone/books/published/pythonds/SortSearch/toctree.html)

## Lab

TBA
