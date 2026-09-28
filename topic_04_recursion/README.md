# Recursion (+ more runtimes + binary search)

<center>
<img src=img/gru.jpg width=400px />

<!--
<br/>
<br/>

[GNU](https://en.wikipedia.org/wiki/GNU_Project) is the name of an open source project that replicates much of the UNIX operating system.
It is a recursive acronym standing for "GNU's Not UNIX".

<img src=img/Strip-Oracle-v-Google-650-finalenglish-4.jpg width=400px />
-->
</center>

**Announcements (Monday 28 Sep):**

1. Word ladder notes:
    1. One of the harder homeworks you'll have
    1. Most of your grade is in the projects
        1. Historically, some students are not able to solve all problems
        1. This is what will separate As/Bs/Cs in the class
        1. Word ladder is worth (very approximately) 5% of your final grade

    1. Recall:
        1. Expect little/no partial credit
        1. Better to submit correct assignment late than incorrect on time
        1. This assignment is 16 points; 1 day late is still an A
        1. I recommend starting early so you can take breaks

            <img src=img/bulb.png width=300px />

    1. About AI:
        1. Ask questions to `llm` / `dic` / `qwen`; cannot use other AI tools like <https://chatgpt.com>
        1. SOTA AIs can "one shot" this problem
        1. I encourage you to solve the problem "manually" as practice
            1. We will see problems later in this class that SOTA AI cannot solve

    1. Debugging tips
        1. Always verify helper functions first
        1. Use 2 terminals always
            1. one to view the code
            1. one to run commands / view the errors
        1. Use vim to open multiple files at once
            1. `:tabe` opens a tab
            1. `gt` = `g`o `t`ab = switch between tabs
        1. Make full use of pytest features
            1. Use `--doctest-modules` to run doctests
            1. Use `--last-failed` (skip successful tests) and `-x` (stop after first failed test)
            1. The tests are **slow**
                1. Run tests in parallel
                   ```
                   $ pip3 install pytest-xdist
                   $ python3 -m pytest -n4
                   ```
                   My solution takes about 5 minutes to run with this command,
                   and 8 minutes to run with the non-parallel command.
                1. They require that your code use the correct list/deque data structure for good asymptotic performance
                1. Test parts of code without using pytest
                    1. I always work on code directly viewing the output before working on pytest
                    1. Use `print` and the `@p` macro liberally when debugging!

## Lecture

1. Recursion
    1. Reference: [chapter 5](https://runestone.academy/runestone/books/published/pythonds/Recursion/TheThreeLawsofRecursion.html)
    1. Every algorithm can be written either
        1. iteratively (using loops)
        1. recursively (by calling itself)
    1. Advantage of recursion:
        1. Easy to prove that algorithms are correct (CSCI148: algorithms)
        1. Easy to prove the runtime of the algorithm using the [Master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
        1. Many algorithms that require while loops are much simpler with recursion (e.g. binary search)
    1. Disadvantage of recursion:
        1. for loops are easier when they are applicable

1. Search
    1. Reference: [chapter 6.1-6.4](https://runestone.academy/runestone/books/published/pythonds/SortSearch/toctree.html)
    1. the most fundamental/important problem of computer science
    1. sequential search:
        1. works for any input
        1. worst case runtime is $\Theta(n)$
    1. binary search
        1. requires the input be sorted; we will see next week that this takes time $\Theta(n \log n)$
        1. worst case runtime is $\Theta(\log n)$ ---- this is really, really fast!!!

## Lab

TBA
<!--
There is no lecture component for the lab session.

See the <https://github.com/mikeizbicki/lab-timeit2> repo for instructions.
-->
