# Travis-CI tutorial

Travis-CI is a tool for automatically running tests on a repo that ensure the code works as expected.
It is a standard tool used by many open source applications in order to maintain code quality.
If you submit code to a project, it will have to pass the travis-ci tests in order for the maintainer to accept your changes.

In this class, we will be using travis as an automatic grading tool for all your programming assignments.
The workflow is described in the following diagram:

<p align=center>
<img src=img/diagram.png?raw=true width=500px>
</p>

Therefore, it is important that you understand how to properly configure travis for your projects,
because if travis is not configured correctly,
you will not get a grade.

## The Fraction repo

The Fraction repo is a modified version of the `Fraction` class taken from [chapter 1.13](https://runestone.academy/runestone/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#a-fraction-class) of the course textbook.
The purpose of the `Fraction` class is to demonstrate how python classes work.
We will talk about classes in detail later,
but for now, we will use this code as a testbed for travis.

I have created a repo containing the fraction class and some other files at: https://github.com/mikeizbicki/fraction

Fork this repo, clone your fork onto the lambda server, and cd into the `fraction` folder.
(Notice that these instructions are much less detailed than the instructions in the previous tutorials.
An important part of this class is to learn how to follow instructions at multiple levels of abstraction.)

If you run `ls -a`, you will see many files contained in your `fraction` folder.
These files are described in the following table.

| file | purpose |
| ---- | --- |
| `.`    | special system file that refers to the current folder |
| `..`   | special system file that refers to the previous folder |
| `Fraction.py` | contains the python code |
| `.git` | this folder contains all the information about the git repo; it is created when running `git init` and should never be modified directly |
| `.gitignore` | this file tells git which files should be ignored; see https://git-scm.com/docs/gitignore for more info |
| `README.md` | contains a description of the project |
| `requirements.txt` | contains a list of python libraries required to run this project |
| `tests` | contains the test cases for the project |
| `.travis.yml` | contains the configuration for travis |

Most python repos have a similar structure to the fraction repo.
The first import file is `requirements.txt`.
For any python repo, we can always install the necessary libraries by running the command

```
$ pip3 install -r requirements.txt
```

In this case, the only library we require is `pytest`, which is a popular framework for testing python programs.

To use pytest, run the command

```
$ python3 -m pytest
```

You should get a rather long output that begins with

```
============================= test session starts =============================
platform linux -- Python 3.6.9, pytest-5.3.2, py-1.8.1, pluggy-0.13.1
rootdir: /home/mizbicki/tmp/firstrepo/fraction
plugins: cov-2.8.1, timeout-1.3.3
collected 9 items                                                                                 

tests/test_fraction.py ......FFF                                        [100%]
```

then contains details about failed test cases, and finally ends with

```
========================= 3 failed, 6 passed in 0.06s =========================
```

In this case, our program passes 6 of the 9 test cases, and fails 3 of them.

## Enable Travis

Before fixing the test cases, we're going to enable travis for the repo.
Travis will automatically run the test cases every time we push a commit to github,
making it easy to check whether all our test cases pass or not.
Travis is able to run these test cases with many versions of python and with many different environments
(e.g. on Windows, Mac, Linux, Android, etc.),
and it does this all in parallel and without using our own personal compute resources.
For large projects, this is hugely valuable.

To enable enable travis for your `fraction` repo,
complete steps 1-3 of the [official travis-ci tutorial](https://docs.travis-ci.com/user/tutorial/).
Steps 4-6 involve creating and adding a `.travis.yml` file to your repository,
which I've already done for you.

To verify that you have successfully configured travis,
visit the URL https://travis-ci.org/mikeizbicki/fraction (but replace `mikeizbicki` with your github username).
All travis builds are public information, so if you visit that link as-is you can see the status of my builds.

## The Travis badge

Most repos that use travis-ci place a *build status image* (more commonly called a *badge*) in their README file.
This image shows the status of the most recent build.
A green badge showing the text "build passing" demonstrates that the repo passes all test cases,
and therefore should instill confidence in potential users of the software that the software is high quality.

The fraction repo's `README.md` file already contains a badge,
but because you forked it from my repo,
the badge is pointing to the wrong location.
In particular,
the first line of the file currently contains the text

```
# The Fraction class ![](https://api.travis-ci.org/mikeizbicki/fraction.svg?branch=master)
```

You need to modify this file so that the URL contains your username instead of `mikeizbicki`.
After doing so, add the file to git, commit the file, and push your changes to github.

## Fix the bug

Now we've completed setting up travis and are ready to fix our code.

To fix the test cases, you will need to edit the `Fraction.py` file.
The problem is with the `__mul__` function, which doesn't currently do anything.
I have included a correctly implemented `__mul__` function in the comments.
Uncomment this code, save the file, and push the updated file to github.

After the changes have been pushed, a new travis build will be automatically initiated.
You should get an email when the build has finished, 
and the email should tell you that your repo now passes all test cases.
Additionally, your travis badge should turn from red to green.
