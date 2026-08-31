# CSCI046: Data Structures and Algorithms

[![](img/smbc.png)](https://www.smbc-comics.com/comic/hansel-and-gretel)

## About the Instructor

See: <https://github.com/mikeizbicki/about-me>

## About the Course

Data structures is the most important course in computer science,
and many of the "classic" CS interview questions come from this course.

In this course, you will do all work on a remote Linux server.

<img src=img/big-data-map2.png width=400px />

The lambda server has:
1. 80 processors
1. 8 GPU
1. 256 GB RAM
1. 2 TB NVME
1. 50 TB RAID array of 16 HDDs

<br/>

<img src=https://raw.githubusercontent.com/mikeizbicki/cmc-advising/master/courses-map.png width=100% />

<br/>

<img src=https://raw.githubusercontent.com/mikeizbicki/cmc-advising/master/iceberg/iceberg.png width=100% />

**Textbook:**

<img src=img/free.jpg width=400px />

All of our textbooks are both [free as in beer](https://en.wiktionary.org/wiki/free_as_in_beer) and [free as in speech](https://en.wiktionary.org/wiki/free_as_in_speech):

1. [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/runestone/books/published/pythonds/index.html) by Brad Miller and David Ranum

1. [Official Python Documentation](https://docs.python.org/)

## Grades

| Assignment Type | Points | Approximate Percentage |
| --------------- | ------ | ---------------------- |
| weekly labs     | `2**1` or `2**2` or `2**3` | 20% |
| weekly projects | `2**2` or `2**3` or `2**4` | 30% |
| weekly quizzes  | `2**2` or `2**3` or `2**4` | 30% |
| oral final exam | `2**6`                     | 20% |

All assignments are designed to help you get a good job:
1. You will build your github portfolio.
1. You will do cool stuff to talk about in interviews (e.g. analyze ALL tweets about covid).
1. The assignments will help you with leetcode-style interview questions.

See <https://github.com/mikeizbicki/cmc-csci046/issues/569> for extra credit opportunities.

Historically, the average student needs to spend about 10 hours per week (outside of class) to get an A.
About half of students will either:
- spend 15-20 hours per week and get an A, or
- spend <10 hours per week and get a B/C.

**Late Work Policy:**

You lose `2**(i-1)` points on every assignment,
where `i` is the number of days late.

> **Example:**
> Homeworks will be due on Tuesdays, so if you submit on Wednesday then `i=1` and you receive a `2**(1-1)` (i.e. `1`) point penalty.
> If you submit on Friday, you receive a `2**(3-1)` (i.e. 4) point penalty.

Do not expect partial credit for incomplete assignments.

It is much better to submit a correct assignment late than an incorrect one on time.

I expect that most students will be submit late assignments at some point.

**Caveats:**

There are 2 "caveat tasks" in this course.
These tasks should be easy, and everyone will get full credit on the task just for completing the task.
If you don't complete one of the tasks, however, your grade will be docked a full letter grade.
(For example, an A- grade would become a B- grade.) 
You have the entire semester (until I submit grades) to complete these tasks.

You can find the details about the caveat tasks at:
1. [caveat_tasks/typespeed.md](caveat_tasks/typespeed.md)
1. [caveat_tasks/culture.md](caveat_tasks/culture.md)

## Academic Integrity

**Technology Policy**

The purpose of this policy is to encourage you to learn how to use AI and other technology effectively.

1. You MAY ONLY use AI tools that we discuss in class using APIs.

    In particular, you MAY NOT use:
    1. web interfaces (e.g. <https://chatgpt.com>, <https://claude.ai>)
    2. subscription-based services (e.g. Claude Code, Codex, CoPilot)

    We will build similarly powerful tools in class from the ground up.

1. You MUST complete all programming assignments on the lambda server.

1. You MUST edit all text in the command line (for example, using vim).

    In particular, you MAY NOT use the GitHub text editor, VSCode, or jupyter notebooks.

1. You MAY NOT share any account credentials with anyone else.

**Collaboration Policy**

The purpose of this policy is to encourage you all to work together like professional programmers work together.

1. You MAY post anything at all to github issues without restriction.

    In particular, you are encouraged to post detailed questions/answers/comments with lots of code. Particularly good posts will be awarded extra credit.

1. You MAY ONLY collaborate with other humans:

    1. in class/lab/office hours,

    1. in the QCL.

    You MAY NOT collaborate with humans in any other context.

1. When collaborating:

    1. You MAY look at another student's code to help them or get high level guidance.

    1. You MAY NOT copy another student's code.

    1. You MUST be the only human to type in code for your assignments.

1. You MAY NOT look at another student's code on github.

    All projects are developed as open source projects, and so the code is published openly online.  The benefits of this model include: (1) you actually learn how to develop/contribute to open source projects; (2) future employers see you have github activity. Please do not abuse this privilege.

## Accommodations Policy

I've tried to design the course to be as accessible as possible for people with disabilities.
(We'll talk a bit about how to design accessible software in class too!)

If you need any further accommodations, please ask.

<!--

Next class should cover:

big pdf assignment:
    and/or short circuiting
    del lines[i] vs remove

word_ladder assignment:
    open the file
    del lines[i]

big-oh:
    big-o of the word ladder with set vs list
    memory usage O(1) vs O(n) vs O(n^2)
    accidentally quadratic

twitter: 
    sys.exit() and bash $?
    use the cowsay and fortune as an example for piping


in the sorting assignment, the _merge function is a dependency of quick_sorted();
passing the test cases for _merge guarantees that the function works,
but you can still get errors inside the function if you have errors outside the functiton

lab processes:

1. add discussion of how the HUP signal is sent differently for different OSes
2. limitted number of processes on the lambda server, show the fork resource exhausted error
3. killall/kill $(...) to kill processes
4. fork bomb
5. debug map.py by looking inside the nohup.out file
6. (un)buffered io, stdout vs stderr, redirection applies only to stdout

No `nohup.out` file in the repo.

introduce superclasses/static methods before the week on BSTs; it's too much to do it all at once; consider doing the deque class

Should probably do doubly linked list as Deque before doing BSTs

Demo something like the insert function in class; it's difficult for students to do the recursive inserts that modify the node values

Should add an insert/remove_min function to the BST/AVLTree class? as an analogy to the heap

Clarify which trees should have duplicates/no duplicates

Add tests to BST/AVLTree/Heap for runtime of operations

-->
<!--
See:
http://nifty.stanford.edu/2020/schwarz-recursion-to-the-rescue/
http://nifty.stanford.edu/2020/denero-typing-test/spec.html
-->

<!--
1. [Yes, the median salary at facebook is $240k](https://www.sfchronicle.com/business/networth/article/Yes-median-pay-at-Facebook-really-is-about-12870786.php)
1. [A detailed analysis of FAANG salaries](https://huyenchip.com/2020/01/18/tech-workers-19k-compensation-details.html), with raw data from [levels.fyi](https://www.levels.fyi/SE/Amazon/Google/Facebook/#)
1. [The high-tech employee antitrust litigation](https://en.wikipedia.org/wiki/High-Tech_Employee_Antitrust_Litigation)
1. [Get jobs from GitHub/HackerNews](https://news.ycombinator.com/item?id=22050802)
1. [/r/cscareerquestions](https://www.reddit.com/r/cscareerquestions/top/)

Other technical articles:

1. [Command-line tools can be faster than a hadoop cluster](https://news.ycombinator.com/item?id=22188877)
1. [intermediate vim](https://dn.ht/intermediate-vim/)
1. [Mike's dotfiles](https://github.com/mikeizbicki/dotfiles)
1. [The missing semester of CS education](https://news.ycombinator.com/item?id=22226380)
1. [Larry Wall's three virtures of a programmer](http://threevirtues.com/)
1. [accidentally quadratic blog](https://accidentallyquadratic.tumblr.com/post/161243900944/mercurial-changegroup-application) and a [windows bug caused by an O(n^2) algorithm](https://news.ycombinator.com/item?id=21743424)
1. [the history of git](https://www.welcometothejungle.com/en/articles/btc-history-git)
1. [timsort](https://svn.python.org/projects/python/trunk/Objects/listsort.txt) - Tim's [Zen of Python](http://www.openbookproject.net/books/bpp4awd/_static/ch10/zen.html)
1. [stackoverflow - why processing sorted arrays is faster even in linear search](https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array)

1. [What every programmer should know about floating-point](https://floating-point-gui.de/)
1. [The lat/lon floating point delusion](https://www.datafix.com.au/BASHing/2019-08-09.html)
1. [The fallacy of premature optimization](https://ubiquity.acm.org/article.cfm?id=1513451)
1. [Computer Science from the Bottom Up](https://www.bottomupcs.com/index.xhtml)

1. https://choosealicense.com/

Library documentation:

1. [timeit](https://docs.python.org/3/library/timeit.html)
1. [collections](https://docs.python.org/3/library/collections.html)
1. [copy](https://docs.python.org/3/library/copy.html)
1. [traceback](https://docs.python.org/3/library/traceback.html)

Programming games:

1. https://vim-adventures.com/
1. The [git game](https://github.com/git-game/git-game) and [git game v2](https://github.com/git-game/git-game-v2)
1. `typespeed` (type this command on the lambda server)
1. [bandit wargames](https://overthewire.org/wargames/bandit/bandit0.html)
-->

