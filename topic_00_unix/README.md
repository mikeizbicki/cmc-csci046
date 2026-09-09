# Topic 00: Unix and the open source workflow

<center>
<a href="https://www.reddit.com/r/linuxmasterrace/comments/3las1l/dilbert_had_it_right_back_in_1995/">
<img width='80%' src='img/dilbert.gif' />
</a>
</center>

**Wed 9 Sep**:

1. Homeworks graded
    1. | hw  | total students | submitted | full credit |
       | --- | -------------- | --------- | ----------- |
       | git tutorial           | 15 | 10 | 7 |
       | llm                    | 15 | 8  | 6 |
       | continuous integration | 15 | 7  | 6 |
    1. if you haven't submitted:
        1. please submit; no late penalty
        1. you are now behind
    1. if you didn't get full credit:
        1. you may resubmit for full credit
    1. common problems:
        1. No pull requests unless asked for: <https://github.com/mikeizbicki/lab-llm>
        1. Be careful with your branches
            1. <https://github.com/asriniketh29/lab-llm>
        1. Never take screenshots of text
            1. <img>
            1. we cannot copy/paste
            1. google cannot index
            1. llms cannot learn from it
            1. correct submission looks something like:
                ```
                $ git log --graph --oneline
                * FFd3762 (HEAD -> master) Merge branch 'new_feature'
                |\  
                | * FFd8ec8 (new_feature) added newfile
                * | FFd980d newfile2
                |/  
                * FFfa06a changed the README
                *   FF4619b solved merge conflict between userinput and master branches
                |\  
                | * FFe2149 updated README
                | * FF14598 added user input
                * | FF6c46b fixed the message bug
                |/  
                * FF24e01 modified the README
                * FF3cc61 added the first code
                ```
        1. Markdown formatting
            1. <https://github.com/jisellenguyen/lab-llm/tree/hw-0-llm>
        1. Always visually inspect your work before submitting
            1. <https://github.com/asriniketh29/continuous-integration>

    1. common theme: "not following instructions exactly"
        1. <https://thethreevirtues.com/>
        1. <https://en.wikipedia.org/wiki/Larry_Wall>
        1. <img src=img/god.jpg width=400px />

1. Quiz Friday!
    1. If you didn't get the message, you're not watching the repo!
    1. Format:
        1. 4 problems.
        1. Fully open note.
        1. First 10 minutes of class.
        1. I will be in class ~20 minutes before start of quiz; everyone is welcome to start quiz early.

## Lecture

We will cover:

1. working on a remote unix server,
1. using the git version control system,
1. using continuous integration to "prove" that your code works.

All text editing must be done in Vim.
We will encounter many instances in this class where more familiar tools like VSCode and Jupyter Notebooks will not work.

<img src=img/vim-productivity.jpg width=500px>

<!--
<img src=img/vim-comic2.webp width=500px>

<img src=img/vim-comic.jpg width=500px>
-->

**Cheat sheets:**

1. [bash](https://files.fosswire.com/2007/08/fwunixref.pdf)
1. [vim](https://github.com/mikeizbicki/ucr-cs100/blob/class-template/textbook/cheatsheets/vim-cheatsheet.pdf)
1. [git](https://education.github.com/git-cheat-sheet-education.pdf)
1. [github pull requests](pull_request.png)

**Quiz details:**

1. There will be a quiz every Wednesday.
1. Your first quiz is next week on Wednesday 9 Sep.
1. The quiz will cover:
    <https://github.com/mikeizbicki/quiz/blob/master/quiz_shell/topic00_intro.pdf>
1. All quizzes are open note.
    I strongly encourage you to complete all of the practice quiz problems and take notes on the practice sheets of paper.

## Lab

**Due date:**

Labs are always due on midnight of the Sunday of the week that they are assigned (e.g. Sep 6 for this lab).

*For this lab only: There will be no late penalty if you miss the due date, but please be reasonable.*

**Pre-lab work:**

1. Create a GitHub account if you do not already have one.

1. Press the watch button on both this repo and <https://github.com/mikeizbicki/about-me>.
    This will ensure you get email notifications whenever a new issue is posted to github.
    All class related communications will happen through github,
    and not through email or canvas.

1. Create a [personal access token (PAT)](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for your github account, and save the PAT to a file for future use.

1. Read and follow the instructions in [the meet and greet issue](https://github.com/mikeizbicki/cmc-csci046/issues/568).

1. Log in to the lambda server.
   Run the command
   ```
   $ vimtutor
   ```
   Complete all instructions in order to learn vim.
   This should take 30-60 minutes.

**Instructions:**

1. Visit the [messages](https://github.com/mikeizbicki/messages) repo and complete the instructions in the README.

1. Complete the [github pull request tutorial](https://github.com/mikeizbicki/pullrequest-tutorial/).

    (This is a modified version of the CSCI040 assignment.
    Those of you who took that class must repeat this assignmnet.)

## Homework

**Due Date:**

Homeworks are always due on the Tuesday of the week after they are assigned (i.e. 8 Sep for this homework).

*For this hw only: I will not apply a late penalty, but please be reasonable.*

**Instructions:**

This week's homework has three parts, all designed to help you get more familiar with the lambda server and github.
Most homeworks in the future will be just one part that is pure programming and less "tutorial".

1. Follow [these instructions](lambda-server.md) to update your lambda server account's settings.

1. Follow [these instructions](https://github.com/mikeizbicki/lab-llm) to get a nice terminal interface to LLMs on the lambda server.

1. This week's homework will teach you how to use continuous integration,
    and prepare you to submit all future assignments.
    You can find the homework at <https://github.com/mikeizbicki/continuous-integration>.

    (If you already completed this assignment in CSCI040, you do not need to redo the steps; just submit the url.)
