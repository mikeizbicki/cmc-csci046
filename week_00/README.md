# week 00: UNIX and the open source workflow

<center>
<a href="https://www.reddit.com/r/linuxmasterrace/comments/3las1l/dilbert_had_it_right_back_in_1995/">
<img width='80%' src='dilbert.gif' />
</a>
</center>

## Lecture

**Learning Objectives:**

1. work on a remote unix server
1. use the git version control system
1. use continuous integration to "prove" that your code works

**Prelecture Work:**

Watch this video:

1. [What is Git and GitHub?](https://www.youtube.com/watch?v=uUuTYDg9XoI)

Print each of these cheatsheets, and have them handy for lecture:

1. [bash](https://files.fosswire.com/2007/08/fwunixref.pdf)
1. [vim](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf)
1. [git](https://education.github.com/git-cheat-sheet-education.pdf)

<!--
## Background

Version control systems are widely used in industry and in open source projects.
They are the tool that lets many programmers work together on complex software.
I don't know what programming language you will use at your future job (it may not even exist yet!),
but I guarantee you will be using version control.
Currently, git is the most popular version control system and we will use git in this course for all your software projects.

Git is an example of a UNIX command line tool.
UNIX is a family of operating systems that are widely popular.
MacOS and Linux are the two most commonly used UNIX operating systems,
but there are many other examples.
In particular, Windows is not a UNIX operating system.
-->

## Lab

Pre-lab work:

1. Create a GitHub account if you do not already have one.
   Log in, and press the "watch" button at the top of this page.
   Read and follow the instructions in Issue #1: the meet and greet thread.

1. Log in to the lambda server.
   Run the command
   ```
   $ vimtutor
   ```
   Complete all instructions in order to learn vim.
   This should take 30-60 minutes.

1. (Optional)
   Play the https://vim-adventures.com game to learn vim while playing a game.
   The first 3 levels are free, but you have to pay to continue playing the game.
   Anyone who completes the entire game gets +1 point extra credit.

1. (Optional)
   Run the command
   ```
   $ typespeed
   ```
   to test your UNIX typing skills.
   Programmers spend lots of time at the keyboard,
   and so it pays to actually be able to type well.
   Anyone who beats my top score gets +1 point extra credit.

Instructions:

1. Complete the [UNIX/git tutorial](git.md)
1. Follow [these instructions](lambda-server.md) to update your lambda server account's settings
1. Complete the [github tutorial](github.md)
