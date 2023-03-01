# topic 6: Object Oriented Programming (OOP) / `class` / iterators / `yield` / generators

## Announcements

1. Grades:
    1. I'm behind on grading (sorry!)
    1. Grader has finally been hired

1. The next 4 homework assignments all work together
    1. You'll create your own data structures / containers
    1. At the end, you'll publish them all as a library (that can be pip installed)
    1. This week's assignment is "easy"
        1. the hard part is getting the concept
        1. there's no tricky edge cases to debug after that
    1. The next three assignments are "hard"
        1. hard concepts and hard tricky edge cases
        1. expect them to take longer than you think
        1. [a common rule of thumb is to multiply your ETA by pi](https://news.ycombinator.com/item?id=28667174)
        1. If you do that, you'll still be way off:
        
            <img src=Strip-Souvenirs-650-finalenglish.jpg width=600px />

## Lecture Notes

1. The `class` keyword lets you define your own data structures

    1. Object Oriented Programming (OOP) is programming with classes

        1. Pronounce OOP as "Oh Oh Pee"

        1. You should think of a class as a "container"

        1. IMNSHO, most OOP programming takes the "using classes" idea too far, and use classes where it's not appropriate

           <img src=1*6rqSrrz_Q5m80KZM9XbqRg.jpeg />
           <br/>
           <br/>

           <img src=8jcj2z7h61741.png width=600px />
           <br/>
           <br/>

           <img src=object-oriented-programming-is-an-exceptionally-bad-idea-which-could-only-63887355.png />

        1. References:
        
            1. Book Reference: [Chapter 1.13](https://runestone.academy/runestone/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html) and [Chapter 2](https://runestone.academy/runestone/books/published/pythonds/ProperClasses/toctree.html)

            1. <https://realpython.com/python3-object-oriented-programming/>

    1. OOP vocabulary:

        1. an "object" is what a variable references;
           an "instance" of a class is an object whose type is that "class";

           in python, the `type` function returns the type of the object

        1. Python uses [duck typing](https://en.wikipedia.org/wiki/Duck_typing)

           <img src=duck.jpg width=400px />

           <img src=dog-duck.jpeg width=400px />

        1. variables within a class are called "attributes" or "properties"

           in other programming languages, there is a distinction between "private" attributes (only accessible within the class) and "public" attributes (accessible everywhere);
           in python, no such distinction exists;
           if an attribute "should" not be accessed outside of the class, in python, we prefix the name with an underscore

           <img src=thinking-about-class-structure-object-oriented-programmers-marxists-also-strong-opinions-66225550.png />

        1. functions within a class are called "methods"

        1. functions that begin/end with double underscores are called "double underscore"/"dunder" methods or "magic" methods

            1. `__init__` is the "constructor" and is called when an instance is first created

               <img src=m3vxtt66jsg61.jpg width=400px />

            1. `__str__` / `__repr__` methods let us "pretty print" our objects;
               `__str__` should be human readable, `__repr__` should be machine readable

               Reference: <https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr>

            1. `__iter__` / `__next__` are functions for creating "iterable" classes", or "generators"

                The for loop
                ```
                for a in b:
                    c
                ```
                is syntactic sugar for
                ```
                _iter = iter(b)
                while True:
                    try:
                        a = next(_iter)
                    except StopIteration:
                        break
                    c
                ```
                where
                ```
                iter = lambda x: x.__iter__()
                next = lambda x: x.__next__()
                ```
                For a detailed technical explanation, see: <https://snarky.ca/unravelling-for-statements/>

            1. we'll see more examples of these dunder methods throughout the rest of the semester

1. PEP8: <https://www.python.org/dev/peps/pep-0008/>

    1. Naming:
        1. PEP = Python Enhancement Proposal
        1. the 8 in flake8 comes from PEP8
        1. the flake in flake8 comes from [pyflakes](https://pypi.org/project/pyflakes/),
            which does [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) to find broken (i.e. flakey) code

    1. class names should be in `CamelCase`

    1. everything else is `snake_case`

1. Three ways to "exit" a function in python

    1. `return`:
       the normal way to stop a function

       immediately stops the current function,
       and control flow never returns to the function

    1. `raise`:
       used to represent errors

       immediately stops the current function and all functions in the call stack;
       the only way to prevent your function from stopping is by using a `try`/`except` block

    1. `yield`:
       turns a function into a generator

       immediately stops the current function,
       and control flow will return to the function

       this is "syntactic sugar" for the `__iter__` and `__next__` class methods used in iterators

    <!--
    1. `sys.exit(n)`: immediately stops the entire program

       must `import sys` to get access to this method;
       all functions in the `sys` module interact directly with the operating system, and may behave subtly different on different operating systems

       on all OSes,
       a value of `n=0` indicates the program was successful;
       any nonzero value indicates the program failed

       this should never be used by "library" code,
       and only used by "application" code;
    -->

## Lab

TBA

<!--
There is no separate graded lab for this week.
We will still have lab, and it will be a chance for everyone to work/ask questions.

1. On github:

    1. **Do not fork the containers repo!**
       We will be using this repo for the next several weeks over homeworks,
       and it will be important in the future that it is not forked.

    1. Instead, create a new repo on your account github account.
       You must name it something other than containers.

1. On the lambda server:

    1. Clone your repo.

    1. Add my repo as a remote.

    1. Pull the contents of my repo into yours.

       Even though your repo is not a fork of mine,
       all the steps for working with git are exactly the same.
       The "fork" abstraction is a github-only thing,
       and not relevant to git at all.

    1. Fix the files in the `containers` folder so that all test cases pass.

1. Submit the link to your github repo on sakai.
-->

<!--
    1. Other popular programming paradigms:

        1. Procedural:
           program executes your code "line-by-line";
           most of what we've been doing so far (and all of CS40) was procedural

        1. Functional:
           when you pass functions to other functions;
           the `filter`/`map`/`reduce` functions (week 1) are examples of "functionals" (a term from math for functions that take functions as arguments; functional analysis is an upper division math class where you study the "linear algebra" of these functions);
           the MapReduce distributed computing paradigm comes from functional programming...
           actually the vast majority of cool new programming techniques these days stem from functional programming

           <img src=programming_languages_curve.png />

           <img src=oop-vs-fn-comics-homer-simpson.png />

        1. Declarative:
           tell the computer what to do rather than how to do it;
           the computer figures out the "how" by itself;
           SQL is the most popular declarative language,
           and widely used in data science

        1. Many others...
           when "good" employers look at resumes,
           they care about how many programing paradigms you know,
           not how many languages you know;
           once you know a language in one paradigm,
           it's trivial to learn a new language in the same paradigm

           Advice:
           1. Paul Graham (founder of ycombinator):
              1. [the python paradox](http://www.paulgraham.com/pypar.html)
                  1. > The language to learn, if you want to get a good job, is a language that people don't learn merely to get a job.

              1. [the 100 year language](http://www.paulgraham.com/hundred.html)
           1. Larry Wall (creater of PERL and hacker legend):
              1. [the 5 programming languages everyone should know](https://www.youtube.com/watch?v=LR8fQiskYII)

           1. Peter Norvig (famous AI researcher and Googler):
              1. [teach yourself programming in 21 days](https://norvig.com/21-days.html)
              
           1. Alan Perlis, first recipient of the Turing Award (like the Nobel Prize for computer science)

              <img src=four-languages-from-forty-years-ago-5-638.jpg />

           1. Me:
              1. Learn Bash/SQL/Julia/Haskell/C

                  1. Bash/SQL: take the big data course (CS143)

                  1. Julia: easy-to-use like python, but fast like C; this is the data science language that everyone will be using 10 years from now

                  1. Haskell: a "true" functional programming language, and the programming language for mathematicians; basically all new Python language features (e.g. list comprehensions, generators) come from Haskell; much better for SWE jobs than DS jobs

                     <img src=haskell.jpeg />

                  1. C: the low level language, and the universal language that all computers/operating systems/other languages can interact with; if you understand C, you "mostly" understand how computers work at the most fundamental level... at some point you'd also need to learn assembly language programming

              1. R/Matlab:
                  1. R: Foundations of Data Science (CS36), classes with Prof. Mark Huber
                  1. Matlab/Octave:  Linear Algebra with Computing (Math 60C), classes with Prof. Chiu-Yen Kao; Octave is an open source implementation of the Matlab programming language, so it's free, and more extensible; it doesn't have a marketing department, however, so corporations/non-CS people like to use Matlab
                  1. from a programming languages perspective, these languages are just like python (procedural languages with some OOP/functional features); the difference is the "culture" of who uses the language: python is used by more "software" people, R by "stats" people, and "Matlab/Octave" by "math" people

              1. Have "strong opinions loosely held"

                 <img src=h81exir2iat01.jpg width=600px />
-->
