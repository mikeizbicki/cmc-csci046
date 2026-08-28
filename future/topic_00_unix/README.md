# Topic 00: Unix and the open source workflow

<center>
<a href="https://www.reddit.com/r/linuxmasterrace/comments/3las1l/dilbert_had_it_right_back_in_1995/">
<img width='80%' src='dilbert.gif' />
</a>
</center>

## Lecture

We will cover

1. working on a remote unix server
1. using the git version control system
1. using continuous integration to "prove" that your code works

<img src=map_of_cs.png width=600px>

All of our work in this class will be done on the "lambda server."
(You should have received an email with login credentials.)
The lambda server has:
1. 80 processors
1. 8 GPU
1. 256 GB RAM
1. 2 TB NVME
1. 50 TB RAID array of 16 HDDs

**Cheat sheets:**

1. [bash](https://files.fosswire.com/2007/08/fwunixref.pdf)
1. [vim](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf)
1. [git](https://education.github.com/git-cheat-sheet-education.pdf)
1. [github pull requests](pull_request.png)

**Quiz details:**

1. You will have a quiz next Wednesday (25 Jan)
1. The format follows the `practice_quiz_X.pdf` files

## Lab

**Due Date:**

Labs are always due on midnight of the Sunday of the week that they are assigned (i.e. January 22 for this lab).

*For this lab only:*
There will be no late penalty if you miss the due date,
but please be reasonable.
This is all important background material,
and I want to ensure that everyone has sufficient time to complete it based on their background experience.

**Pre-lab work:**

1. Create a GitHub account if you do not already have one.
   Log in, and press the "watch" button at the top of this page.
   This will ensure you get email notifications whenever I post new issues to github.

1. Read and follow the instructions in [the meet and greet issue](https://github.com/mikeizbicki/cmc-csci046/issues/324).

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
   Play the <https://vim-adventures.com> game to learn vim while playing a game.
   The first 3 levels are free, but you have to pay to continue playing the game.
   Anyone who completes the entire game before the end of the semester gets +1 point extra credit.

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

1. Visit the [messages](https://github.com/mikeizbicki/messages) repo and complete the instructions in the README.

1. Complete the [unix/git tutorial](git.md).

1. Follow [these instructions](lambda-server.md) to update your lambda server account's settings.

1. Complete the [github pull request assignment](github.md) (we'll cover the details of how to do this Monday, so you don't need to complete it until then)

<!--
**Lab Submission:**

Submit a link to your pull request in sakai.
(I need the link since your github usernames are pseudonymous, and I won't know who to give credit for the lab without the link.)
-->

## Homework

Homeworks will generally be posted into the `homework` [git submodule](https://www.atlassian.com/git/tutorials/git-submodule) for each week.
Homeworks are always due on Tuesday of the week after they are assigned (i.e. Jan 24 for this homework).

*For this hw only: There will be no late penalty if you miss the due date, but please be reasonable.*


