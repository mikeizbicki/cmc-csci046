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

There is no lecture component for the lab session.

See the <https://github.com/mikeizbicki/lab-timeit2> repo for instructions.
