# topic 00: unix and the open source workflow

<center>
<a href="https://www.reddit.com/r/linuxmasterrace/comments/3las1l/dilbert_had_it_right_back_in_1995/">
<img width='80%' src='dilbert.gif' />
</a>
</center>

## Lecture

We will cover how to

1. work on a remote unix server
1. use the git version control system
1. use continuous integration to "prove" that your code works

Cheat sheets:

1. [bash](https://files.fosswire.com/2007/08/fwunixref.pdf)
1. [vim](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf)
1. [git](https://education.github.com/git-cheat-sheet-education.pdf)
1. [github pull requests](pull_request.png)

## Lab

**Due Date:**

Labs are always due on midnight of the Sunday of the week that they are assigned (i.e. January 22 for this lab).

Since this is the first lab, there will be no late penalty applied if you cannot complete it in time.

**Pre-lab work:**

1. Create a GitHub account if you do not already have one.
   Log in, and press the "watch" button at the top of this page.
   Read and follow the instructions in [the meet and greet issue](https://github.com/mikeizbicki/cmc-csci046/issues/137).

    1. (optional)
       If you're not familiar with git/github, then I recommen watching the video [What is Git and GitHub?](https://www.youtube.com/watch?v=uUuTYDg9XoI) for more background.

1. Log in to the lambda server.
   Run the command
   ```
   $ vimtutor
   ```
   Complete all instructions in order to learn vim.
   This should take 30-60 minutes.

   Vim is famous for having a steep learning curve,
   and has inspired lots of memes/comics:

   <img src=vim-productivity.jpg width=500px>

   <img src=vim-comic2.webp width=500px>

   <img src=vim-comic.jpg width=500px>

    1. (Optional)
       Play the https://vim-adventures.com game to learn vim while playing a game.
       The first 3 levels are free, but you have to pay to continue playing the game.
       Anyone who completes the entire game gets +1 point extra credit.

**Instructions:**

<!--
1. *Part I: Sending messages.*

    The terminal allows sending messages between 
-->

   <!--
1. Run the command
   ```
   $ typespeed
   ```
   to test your unix typing skills.
   Programmers spend lots of time at the keyboard,
   and so it pays to actually be able to type well.
   -->

1. Complete the [unix/git tutorial](git.md)

1. Complete the [github pull request assignment](github.md)

1. Follow [these instructions](lambda-server.md) to update your lambda server account's settings

**Lab Submission:**

Submit a link to your pull request in sakai.
(I need the link since your github usernames are pseudonymous, and I won't know who to give credit for the lab without the link.)

## Homework

**Due date:**

Homeworks are always due on midnight of the Sunday of the week that they are assigned (i.e. January 24 for this homework).

Since this is the first homework assignment, there will be no late penalty applied if you cannot complete it in time.

**Instructions:**

See the [homework](homework) git submodule.
