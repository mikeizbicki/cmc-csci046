# CSCI046: Data Structures and Algorithms

## About the Instructor

|||
|-|-|
| Name | Mike Izbicki (you can call me Mike) |
| Email | mizbicki@cmc.edu |
| Office | Adams 216 |
| Office Hours | Monday 9:00-10:00AM, Tuesday/Thursday 2:30-3:30PM, or by appointment ([see my schedule](https://izbicki.me/schedule.html));<br/> if my door is open, feel free to come in |
| Webpage | [izbicki.me](https://izbicki.me) |
| Research | Machine Learning (see [izbicki.me/research.html](https://izbicki.me/research.html) for some past projects) |
| Fun Facts | grew up in San Clemente, 7 years in the navy, phd/postdoc at UC Riverside, taught in [DPRK](https://pust.co) |

## About the Course

This is a second semester course in computer science designed for students who have previously taken either CS40 at CMC or CS5 at Mudd.

This course is required for the computer science sequence,
and optional for the data science sequence.
It will be required for the data science major (if/when it gets approved).

<!--Data structures is the most important course of any computer science program.-->

**Learning Objectives:**

Primary objectives:

1. Learn basic devops and how open source software is developed
1. Be able to answer the following three questions about an algorithm:
    1. Is it correct?
    1. How much resources does it consume? (time, memory, money, etc.)
    1. Can we do better?

Secondary objectives:

1. Learn basic shell programming
1. More experience with python programming
1. Solve the questions asked in programming interviews and contests
1. Introduction to the mathematics of programming (overlap with discrete math)
1. Introduction to the hacker culture

Differences between this course and HMC's CSCI060HM/CSCI070HM:

1. This course does not cover low-level memory management (C/C++ programming languages)
1. This course is more practical
1. There is no lab section

**Textbook:**

1. [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/runestone/books/published/pythonds/index.html) by Brad Miller and David Ranum
2. [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by Dasgupta, Papadimitriou, and Vazirani

**Optional Readings:**

Advice on how to be a good programmer:

1. [Peter Norvig](https://norvig.com/21-days.html) (AI researcher and senior engineer at Google)
1. [Paul Graham](http://www.paulgraham.com/college.html) (Founder of YCombinator startup incubator); [being a noob](http://paulgraham.com/noob.html)
1. [Jeff Atwood](https://blog.codinghorror.com/how-to-become-a-better-programmer-by-not-programming/) (Founder of stackoverflow.com)
1. [Eric Steven Raymond, better known as esr](http://www.catb.org/esr/faqs/hacker-howto.html) (a famous hacker)

How to make money/get a good job:

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
<!--
1. [O(n^2) again](https://news.ycombinator.com/item?id=21743424)
1. [What every programmer should know about floating-point](https://floating-point-gui.de/)
1. [The lat/lon floating point delusion](https://www.datafix.com.au/BASHing/2019-08-09.html)
-->
<!--1. [The fallacy of premature optimization](https://ubiquity.acm.org/article.cfm?id=1513451)-->
<!--1. [Computer Science from the Bottom Up](https://www.bottomupcs.com/index.xhtml)-->

Cheat sheets:

1. [bash](https://files.fosswire.com/2007/08/fwunixref.pdf)
1. [vim](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf)
1. [git](https://education.github.com/git-cheat-sheet-education.pdf)

Programming games:

1. https://vim-adventures.com/
1. The [git game](https://github.com/git-game/git-game) and [git game v2](https://github.com/git-game/git-game-v2)
1. `typespeed` (type this command on the lambda server)
1. [bandit wargames](https://overthewire.org/wargames/bandit/bandit0.html)

## Schedule

### Lecture

| Week | Date         | Topic                                           | Reading       |
| ---- | ------------ | ----------------------------------------------- | ------------- |
| 1    | Tues, 21 Jan | Intro to shell / vim / git / travis             |               |
| 1    | Thur, 23 Jan | Intro to shell / vim / git / travis             |               |
| 2    | Tues, 28 Jan | Intro to shell / vim / git / travis             |               |
| 2    | Thur, 30 Jan | Python features                                 | MR 1-2        |
| 3    | Tues, 04 Feb | Analysis I                                      | MR 3, DPV 0.3 |
| 3    | Thur, 06 Feb | Analysis II                                     | [PythonWiki](https://wiki.python.org/moin/TimeComplexity) |
| 4    | Tues, 11 Feb | Basic data structures: stack                    | MR 4.1-4.9    |
| 4    | Thur, 13 Feb | Basic data structures: queue                    | MR 4.10-4.23  |
| 5    | Tues, 18 Feb | Recursion I                                     | MR 5.1-5.10   |
| 5    | Thur, 20 Feb | Recursion II                                    |               |
| 6    | Tues, 25 Feb | Sorting I                                       | MR 6.6-6.12   |
| 6    | Thur, 27 Feb | Sorting II                                      | [stackoverflow](https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array) |
| 7    | Tues, 03 Mar | Sorting: binary search                          | MR 6.3-6.4    |
| 7    | Thur, 05 Mar | Sorting: hash functions                         | MR 6.5        |
| 8    | Tues, 10 Mar | Recursion: divide and conquer                   |               |
| 8    | Thur, 12 Mar | Recursion: divide and conquer                   |               |
| 9    | Tues, 17 Mar | **NO CLASS:** Spring Break                      |               |
| 9    | Thur, 19 Mar | **NO CLASS:** Spring Break                      |               |
| 10   | Tues, 24 Mar | Trees I                                         | MR 7.1-7.7    |
| 10   | Thur, 26 Mar | Trees II                                        |               |
| 11   | Tues, 31 Mar | Trees: BST                                      | MR 7.11-7.14  |
| 11   | Thur, 02 Apr | Trees: AVL                                      | MR 7.15-7.17  |
| 12   | Tues, 07 Apr | Trees: Heaps                                    | MR 7.8-7.10   |
| 12   | Thur, 09 Apr | Graphs: representations                         | MR 8.1-8.6    |
| 13   | Tues, 14 Apr | Graphs: traversals                              | MR 8.7-8.18   |
| 13   | Thur, 16 Apr | Graphs: Dijkstra                                | MR 8.20-8.21  |
| 14   | Tues, 21 Apr | Graphs: Prim                                    | MR 8.22       |
| 14   | Thur, 23 Apr | Graphs: Kruskal                                 |               |
| 15   | Tues, 28 Apr | Recursion: dynamic programming (matrix mul)     | DPV 6.5       |
| 15   | Thur, 30 Apr | Recursion: dynamic programming (knapsack)       | DPV 6.4       |
| 16   | Thur, 05 May | P vs NP                                         | DPV 8.1, 8.2  |
| 16   | Thur, 07 May | **NO CLASS:** Reading Day                       |               |

<!--
More reading:
https://choosealicense.com/
RSA: DPV 1.4.2
(karatsuba) DPV 1.1, 2.1
(strassen)  DPV 2.5
-->

### Assignments

We will have approximately 1 assignment per week in this course according to the following schedule.

| Assignment | Type    | Points | Topic                           |
| ---------- | ------- | ------ | ------------------------------- |
| 1          | project | 10     | Unix/Git tutorial               |
| 2          | math    | 10     | Analysis/Big-O                  |
| 3          | project | 10     | RPN calculator (stack)          |
| 4          | math    | 10     | recursion/queue/deque/list      |
| 5          | project | 10     | implement sorts                 |
| 6          | math    | 10     | divide and conquer              |
| 7          | project | 10     | twitter data analysis           |
| 8          | test    | 20     | midterm                         |
| 9          | project | 10     | BST                             |
| 10         | project | 10     | AVL tree                        |
| 11         | project | 10     | Heaps                           |
| 12         | math    | 10     | Graphs                          |
| 13         | project | 10     | Dijkstra                        |
| 14         | project | 10     | Knapsack                        |
| 15         | test    | 20     | Final                           |

**Late Work Policy:**

You lose 10% on the assignment for each day late.
If you have extenuating circumstances, contact me in advance of the due date and I may extend the due date for you.

It is usually better to submit a correct assignment late than an incorrect one on time.

**Collaboration Policy:**

For project/math assignments:
you may use any resources you like and discuss with whomever you like.
Learning the material in this course is your responsibility,
and I don't want to put any artificial restrictions on any of the assignments that will get in your way.


Tests will be take home and open notes.
The only restriction is you are not allowed to talk to other students in the class about the contents.

**Technology Policy:**

You must use either vim or emacs to complete all programming assignments.

You must not share your lambda-server password with anyone else.

**Extra credit:**

If you submit a pull request to this repo that gets accepted (e.g. you fix a typo),
then you will get extra credit.
The first time you do this, you will get 1 point of extra credit;
subsequent times you will get less.

If you make a contribution to an open source project during the course,
you will get extra credit depending on the magnitude of your contribution.
See https://up-for-grabs.net for some projects that are looking for new contributors.

<!--
Possible other assignments:
programming: analyze all tweets
math: NP-hard problems
programming: learn git
programming, fibonacci divide and conquer (see Dasupta 0.4)
-->

<!--
## Self Grading

[An outlook on self-assessment of homework assignments in higher mathematics education](https://link.springer.com/article/10.1186/s40594-018-0146-z)

Also *Your* Job to Learn! Helping Students Reflect on their Learning Progress

Should you Allow your Students to Grade their own Homework?

Peer and Self Assessment in Massive Online Classes
-->

## Accommodations for Disabilities

I want you to succeed and I'll make every effort to ensure that you can.
If you need any accommodations, please ask.

If you have already established accommodations with Disability Services at CMC, please communicate your approved accommodations to me at your earliest convenience so we can discuss your needs in this course. You can start this conversation by forwarding me your accommodation letter. If you have not yet established accommodations through Disability Services, but have a temporary health condition or permanent disability (conditions include but are not limited to: mental health, attention-related, learning, vision, hearing, physical or health), you are encouraged to contact Assistant Dean for Disability Services & Academic Success, Kari Rood, at disabilityservices@cmc.edu to ask questions and/or begin the process. General information and the Request for Accommodations form can be found at the CMC DOS Disability Service’s website. Please note that arrangements must be made with advance notice in order to access the reasonable accommodations. You are able to request accommodations from CMC Disability Services at any point in the semester. Be mindful that this process may take some time to complete and accommodations are not retroactive. It is important to Claremont McKenna College to create inclusive and accessible learning environments consistent with federal and state law. If you are not a CMC student, please connect with the Disability Services Coordinator on your campus regarding a similar process.

