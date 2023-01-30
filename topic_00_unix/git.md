# Unix/Git Tutorial

This tutorial will walk you through how basic unix and git commands work.
It will prepare you to complete the first quiz in the class.

You should complete this tutorial on the lambda server by typing all commands within code blocks into your terminal.

> **NOTE:**
> There is a lot of material in these instructions related to git that we have not covered in class.
> That is intentional.
> The purpose of this assignment is not just to learn git,
> but also to learn how to follow tutorials about material that you have never learned about before.

## Creating your first repo

Create a folder named `firstrepo` and `cd` into it:

```
$ mkdir firstrepo
$ cd firstrepo
```

Verify that the folder is empty by running
```
$ ls
$ ls -a
```

This folder will be the home of your first git repository.
Run the following command to initialize it:

```
$ git init
```

All the information for the git repository is stored in a hidden folder called `.git`.
The folder is hidden because it begins with a `.`.
By default, the `ls` command does not display these hidden folders.
To display them, you must pass the `-a` flag (the "a" stands for "all").
Compare the results of the following two commands:

```
$ ls
$ ls -a
```

Now we are ready to add some files into our repo.
Every repo in this class must have a `README` file.
`README` files describe what the project is about for new users.

Create the file using the following command:

```
$ touch README
```

The `touch` command is a standard unix command.
If the input file does not already exist, `touch` creates an empty file with that name.
If the file does already exist, it updates the file's timestamp to the current time.
The `ls -l --full-time` command displays the full information about each file in the current directory.
Run the following commands:

```
$ ls -l --full-time
$ touch README
$ ls -l --full-time
```

Notice how the timestamp in the first `ls` is different than the timestamp in the second `ls`.
Now run the command
```
$ ls -l
```
Can you figure out what the `--full-time` flag did?

We've created our first file, but git doesn't know about it yet.
Run the command:

```
$ git status
```

In the output, there is a section labeled `Untracked files`.
Notice that the `README` file is in this section.
We need to add it into our project using the command:

```
$ git add README
```

Now, when we run `git status`, there is a section labeled `Changes to be committed` with the `README` file underneath it.

Whenever we finish a task in our repo, we *commit* our changes.
This tells git to save the state of the repo so that we can come back to it later if we need to.
Commit your changes using the command:

```
$ git commit -m "my first commit"
```

> **NOTE:**
> Depending on your settings, you may get a message that looks like
> 
> ```
> *** Please tell me who you are.
> 
> Run
> 
>   git config --global user.email "you@example.com"
>   git config --global user.name "Your Name"
> 
> to set your account's default identity.
> Omit --global to set the identity only in this repository.
> 
> fatal: empty ident name (for <test@cmc.edu>) not allowed
> ```
> 
> If this happens, you will need to run both `git config` commands above to set your email and username.

Every commit needs a *commit message* that describes what changes we made in the repo.
Writing clear, succinct, informative commit messages is one of the keys to using git effectively.
In this case, we passed the `-m` flag to git, so the commit message was specified in the command line.
If we did not pass a flag, then git would have opened the vim editor for us to type a longer commit message.
Whether or not you use the `-m` flag is purely a matter of style, but in my experience, it's usually easier to add the flag.

## Creating a Unix python program

Let's add some actual code to our project.
Use vim to create a file `message.py` with the following code:

```
#!/usr/bin/python3

def main(message):
    print(f'{message} world!')

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--message',choices=['hello','goodbye'])
    args = parser.parse_args()
    main(args.message)
```

This python file is using several things that you may not have seen before:

1. The first line in the file above is called the *shebang*.
   This line is not used by python (it is a python comment because it starts with `#`),
   but is instead used by the unix shell to know what program should be used to run this file.
   In this case, the shebang says to use the `python3` command.
   You will see these shebang lines frequently in python programs,
   but for our purposes you can ignore them.
   If you're interested, however, you can read [this stackoverflow question](https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take) for more details.

1. The `__name__` variable is a special built-in python variable that is always defined.
   (All variables surrounded by `__` are special built-in variables.)
   `__name__` is set to `'__main__'` whenever the python script is run from the command line.
   Thus, for example, if we run the command `python3 message.py`, then `__name__ == '__main__'` will evaluate to `True` and the program will enter the body of the if statement.

1. The print statement `print(f'{message} world!')` uses python f-strings,
   which is a new feature added into python 3.6.
   Whenever a string literal begins with `f`,
   any python code within curly braces will be evaluated and substituted into the string.
   See [this tutorial](https://cito.github.io/blog/f-strings/) if you want to learn more.

1. The argparse library is used to pass command line arguments to python programs.
   We'll see some examples of how the argparse library works in the following sections.

After you've saved your `message.py` file,
run the program with the command

```
$ python3 message.py --message=hello
```

You should get an output that looks like

```
hello world!
```

The string `--message=hello` is called a *command line argument*.
The argparse library is a standard library that comes with python and is used for parsing these command line arguments.
In our `message.py` file, we defined an argument called `--message` and said that it can have two values:
either `hello` or `goodbye`.
For example, we could run the command

```
$ python3 message.py --message=goodbye
```

to get the output

```
goodbye world!
```

But if we try to run the command

```
$ python3 message.py --message=hi
```

we get an output that looks like

```
usage: message.py [-h] [--message {hello,goodbye}]
message.py: error: argument --message: invalid choice: 'hi' (choose from 'hello', 'goodbye')
```

Notice in particular that the `main` function did not get executed.
When the `parse_args` function is executed,
the `argparse` module checks if the command line arguments are valid.
If they are not, then the program prints an error message describing how to use the software correctly and then aborts.

You can also run your program by launching python interactively, importing your module into the repl, and the calling the main function with the following commands:

```
$ python3 -i message.py
>>> import message
>>> message.main('hello')
```

> **NOTE:**
> Lines beginning with `$` are shell commands,
> and lines beginning with `>>>` are python commands.
> This is a standard convention that most authors follow.
> In order to exit the Python interpreter, press `CTRL+D` on an empty line.

Now let's add `message.py` to the repo and commit your changes:

```
$ git add message.py
$ git commit -m "added the first code"
```

> **WARNING:**
>
> If you run the `ls` command again, you will notice that a file called `__pycache__` has appeared in your directory.
> YOU SHOULD NEVER ADD THE `__pycache__` FILE TO A GIT REPO.
> This file contains something called *bytecode* created by the `python3` command to make running programs faster.
> Only plaintext files should ever be added into a git repo.

Let's make one more commit so we'll have something to play with.
Run the command:

```
$ echo "This program prints \"hello git\"" > README
```

> **NOTE:**
> The `echo` command prints its arguments to a special file called `stdout`.
> By default, `stdout` is your terminal window (called a `tty` in unix).
> Thus, running the command `echo this is a test` will print `this is a test` to the screen.
> The `>` command is called output redirection.
> Output redirection changes `stdout` to point to a file, instead of the screen.
> Therefore, placing `> README` at the end of the `echo` command causes the output to be placed into the `README` file instead of displayed on the screen.

The command `cat` prints the contents of a file.
Verify that your `README` file has changed using the command:

```
$ cat README
```

Now run:

```
$ git commit -m "modified the README"
```

Uh oh!

We got an error message that ends with `no changes added to the commit`.

Every time you modify a file, if you want that file included in the commit,
you must explicitly tell git to add the file again.
This is because sometimes programmers want to commit only some of the modified files.
We can commit the changes by:

```
$ git add README
$ git commit -m "modified the README"
```

## Traveling through time

Okay!

Now we're ready to take advantage of git's power.

Run the command:

```
$ git log
```

This gives us a history of all our commits.
For each commit, there are four pieces of information.
The first is the commit identifier.
This is a long hexadecimal sequence such as `093d5fa3c60ce204b6ddba86d4f9c355b4856f10`.
(Technically, this is a [SHA1 hash of your commit](https://en.wikipedia.org/wiki/SHA1).
This hash is "cryptographically secure", meaning that it is practically guaranteed to be unique.)
Next is the author of the commit, the date of the commit, and the commit message.

Sometimes, we want to look at what the state of our repo was in a previous commit.
There are many reasons this is useful.
For example, maybe your latest changes broke some functionality and you want to see what working code looked like.
Or, maybe a user of your code reported a bug, but they're using an old version of the software;
we need to look at the old version of the code to reproduce the bug.

We can inspect the previous state of our code using the `git checkout` command.
This command takes as a parameter the hash of the commit we want to inspect.
For me, the hash of the commit with message `my first commit` is `a20aef2096d98ab53d1495f823409e2cc8cd54b9`.
So to inspect that commit, I would run:

```
$ git checkout a20aef2096d98ab53d1495f823409e2cc8cd54b9
```

> **NOTE:**
> You should replace the hash above with the hash of your `my first commit`

Now let's see what happened.
Run the command:

```
$ cat README
```

The file is empty again!

Now run:

```
$ ls -l
```

Your `message.py` file disappeared!
All of the files tracked by git have returned to their previous state.

Let's restore all those changes.
Run the command:

```
$ git checkout master
```

And verify that our changes have been restored:

```
$ cat README
$ ls -l
```

## Git repos are directed acyclic graphs (DAGs)

Another important use of version control systems is working with multiple versions of the same project at once.
This is VERY useful.
You'll be required to do this in future homework assignments (and all throughout your illustrious careers), so pay attention!

Every version of our repo is called a *branch*.
A project can have many branches, and every branch can be completely different than every other branch.
List the branches in your current project using the command:

```
$ git branch
```

This should list just a single branch called `master`.
This branch was created for you automatically when you ran the `git init` command.

One way to think of branches is as a nice label for your commit hashes.
Your `master` branch currently points to your commit with the message `modified the README`.
That's why when we ran `git checkout master` above,
it restored our project to the state of that commit.
We could also have used `git checkout [hash]`,
if you replaced `[hash]` with the appropriate hash value.
But that's much less convenient.
When you use `git checkout` in the future, you will usually be using it on branch names.

From now on, we'll be drawing pictures of our git repos so you can visualize what's going on.
Currently, our repo looks like:

<p align=center>
<img src="img/3.png?raw=true">
</p>

The purple boxes represent all the commits we've done, and the blue box represents a branch.

Every time we add a new feature to a project, we create a branch for that feature.
Let's create a branch called `userinput` in our project by:

```
$ git branch userinput
```

Verify that our branch was created successfully:

```
$ git branch
```

You should see two branches now.
There should be an asterisk next to the master branch.
This tells us that master is the currently active branch,
and if we commit any new changes, they will be added to the master branch.
(That is, `master` will change to point to whatever your new commit is.)

Our repo DAG now looks like:

<p align=center>
<img src="img/4.png?raw=true">
</p>

Switch to our new branch using the command:

```
$ git checkout userinput
```

Now run

```
$ git branch
```

and verify that the asterisk is next to the `userinput` branch.
Since the only thing you did was switch branches, the repo DAG looks almost the same.
The only difference is the asterisk has moved.

<p align=center>
<img src="img/5.png?raw=true">
</p>

Let's modify our `message.py` file so that it asks the user their name before saying hello:

```
#!/usr/bin/python3

def main(message,input_name):
    if input_name:
        print('enter your name')
        name = input()
    else:
        name = 'world'
    print(f'{message} {name}!')

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--message',choices=['hello','goodbye'])
    parser.add_argument('--input_name',action='store_true')
    args = parser.parse_args()
    main(args.message,args.input_name)
```

Test your code by running the command

```
$ python3 message.py --message=hello
```

You should get the same output as you got before:

```
hello world!
```

But now if you run the command

```
$ python3 message.py --message=hello --input_name
```

The program will ask you for your name and greet you by name:

```
enter your name
Mike
hello Mike!
```

Notice that the command line argument `--input_name` does not get assigned a value.
Instead, the `args.input_name` variable will default to `False`;
but when the `--input_name` command line argument is present,
then `args.input_name` will be set to `True`.
These `True`/`False` command line arguments are typically called *command line flags*,
or just *flags* for short.

Now, commit our changes to the current working branch the same way we committed them before:

```
$ git add message.py
$ git commit -m "added user input"
```

Before this commit, the `userinput` and `master` branches were pointing to the same commit.
When you run this command, the `userinput` branch gets updated to point to this new commit.
Now your DAG looks like:

<p align=center>
<img src="img/6.png?raw=true">
</p>

Let's verify that our changes affected only the `userinput` branch and not the `master` branch by running the following commands:

```
$ git checkout master
$ cat message.py
$ git checkout userinput
$ cat message.py
```

Notice that the contents of `message.py` are different depending on which branch you are on.

We're not done with this feature yet.
Whenever you add a feature, you should also update the documentation!

Ensure that you are in the `userinput` branch,
and update the `README` file with the command:

```
$ echo "This program asks the user for their name, then says hello." > README
```

And add it to the repo:

```
$ git add README
$ git commit -m "updated README"
```

Your repo DAG now looks like:

<p align=center>
<img src="img/7.png?raw=true">
</p>

We say that `userinput` is "two commits ahead" of `master` because we have created two commits on the `userinput` branch.

A typical software engineer might make anywhere from one new branch per week to 5 or more new branches per day.
The amount of branching depends on the types of programs being developed and the difficulty of the features being added.

## Fixing a bug

Wait!

While we were working on our `userinput` branch, someone reported a bug in our `master` branch.
To fix this bug, we first checkout our master branch:

```
$ git checkout master
```

The bug is that our program has bad output when the user does not pass in the `--message` command line argument.
If someone types the command

```
$ python3 message.py
```

then they get the output

```
None world!
```

which doesn't make a lot of sense.

To fix this bug, we'll create a `bugfix` branch and check it out.
Ensure that you are currently on the master branch,
then run the commands

```
$ git branch bugfix
$ git checkout bugfix
```

Here's the resulting DAG.
Notice that the `bugfix` branch starts where the `master` branch was because we switched to `master` before creating `bugfix`.

<p align=center>
<img src="img/8.png?raw=true">
</p>

Now we're ready to edit the code.
Change the line

```
   parser.add_argument('--message',choices=['hello','goodbye'])
```

to read

```
   parser.add_argument('--message',choices=['hello','goodbye'],default='hello')
```

This changes the default value of `message` from `None` to `'hello'`.
The default value of every command line argument in `argparse` is `None` unless you specify otherwise.
Bugs like this are extremely common in code.
Libraries like `argparse` have many options that you can use,
and it is very easy to forget to specify all the options
(or to not even know about all the options that you might need to set).
You will have bugs like this in every program you ever write,
and that's okay.
Most programs---especially programs with millions of lines of code---are not bug free.

Verify that your changes worked by running the command

```
$ python3 message.py
```

and ensure you get the output

```
hello world!
```

Once you've completed those changes,
add `message.py` to the staging area and commit your change.

```
$ git add message.py
$ git commit -m "fixed the message bug"
```

Since you made the commit on the `bugfix` branch,
your DAG splits off in another direction and now looks like this:

<p align=center>
<img src="img/9b.png?raw=true">
</p>

Notice that the DAG is no longer a linear structure, but looks like a tree with branches.
This is where the name branch comes from.

## Merging branches

We want our users to get access to the fixed software,
so we have to add our `bugfix` code into the `master` branch.
This process is called *merging* the `bugfix` into the `master` branch.

In this case it is a simple procedure.

First, checkout the `master` branch:

```
$ git checkout master
```

Then run the command:

```
$ git merge bugfix
```

This automatically updates the modified files.

Your DAG will now look like this:

<p align=center>
<img src="img/10b.png?raw=true">
</p>

Using branches like this to patch bugs is an extremely common pattern.
Whether you're developing open source software or working on Facebook's user interface,
this is the same basic procedure you will follow.

With real bugs on more complicated software, bug fixes won't be quite this easy.
They might require editing several different files and many commits.
It might take us weeks just to find out what's even causing the bug!
By putting our changes in a separate branch,
we make it easy to have someone fixing the bug while someone else is adding new features.

## Merge conflicts

Our `userinput` feature is also ready now.
We've tested it and are sure it's working correctly.
It's time to merge this feature with the `master` branch.
Run the commands:

```
$ git checkout master
$ git merge userinput
```

Ouch!

We get an error message saying:

```
Auto-merging message.py
CONFLICT (content): Merge conflict in message.py
Automatic merge failed; fix conflicts and then commit the result.
```

This error is called a *merge conflict* and is one of the hardest concepts for new git users to understand.
Why did this happen?

In our `bugfix` branch above, git automatically merged the `message.py` file for us.
It could do this because the `message.py` file in the `master` branch did not change after we created the `bugfix` branch.
Unfortunately, after we merged the `bugfix` branch into master, this changed the `message.py` file.
Now when git tries to merge our changes from the `userinput` branch, it doesn't know which parts to keep from `userinput`, and which parts to keep from `bugfix`.
We have to tell git how to do this manually.

If you inspect the contents of the `message.py` file, you'll see something like:

```
#!/usr/bin/python3

def main(message,input_name):
    if input_name:
        print('enter your name')
        name = input()
    else
        name = 'world'
    print(f'{message} {name}!')

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
<<<<<<< HEAD
    parser.add_argument('--message',choices=['hello','goodbye'],default='hello')
=======
    parser.add_argument('--message',choices=['hello','goodbye'])
    parser.add_argument('--input_name',action='store_true')
>>>>>>> master
    args = parser.parse_args()
    main(args.message,args.input_name)
```

As you can see, the file is divided into several sections.
Any line not between the `<<<<<<<<` and `>>>>>>>>` lines is common to both versions of `message.py`.
The lines between `<<<<<<<< HEAD` and `=======` belong only to the version in the currently checked out branch (in this case, `master`).
In git terminology, `HEAD` is the currently checked out branch and refers to the `*` in the DAGs we've been drawing.
And the lines between `=======` and `>>>>>>>> userinput` belong only to the `userinput` branch.

The key to solving a merge conflict is to edit the lines between `<<<<<<<` and `>>>>>>>` to include only the correct information from each branch.
In our case, we want the `--message` line from the `master` branch,
and the `--input_name` line from the `userinput` branch.
So we should modify the `message.py` file to be:

```
#!/usr/bin/env python3

def main(message,input_name):
    if input_name:
        print('enter your name')
        name = input()
    else
        name = 'world'
    print(f'{message} {name}!')

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--message',choices=['hello','goodbye'],default='hello')
    parser.add_argument('--input_name',action='store_true')
    args = parser.parse_args()
    main(args.message,args.input_name)
```

Changing the `message.py` file so that it contains the correct lines from each of the merged branches is called *resolving* the merge conflict.
Once we have resolved this conflict, we can finalize our merge.
We first tell git that we've resolved the conflict by adding the conflicting files,
then we perform a standard commit:

```
$ git add message.py
$ git commit -m "solved merge conflict between userinput and master branches"
```

And your DAG looks like:

<p align=center>
<img src="img/11b.png?raw=true"
</p>

As you can see, resolving merge conflicts is a difficult process.
Most projects try to avoid merge conflicts as much as possible.
A simple strategy for doing this is using many small source files rather than a few large files.
This makes it more likely that multiple branches will not edit the same files.

Of course, in most projects merge conflicts will be inevitable.
That's just the reality of working on large projects with many team members.

## Cleaning up

Programmers often talk about maintaining *clean* git histories.
We say a repo has a clean history if it is easy to see who is working on what,
and that there is no extra stuff in the history that we don't need.

Since we're done with the `bigfix` and `userinput` branches,
we should delete them with the `git branch -d command`.

Run the following commands to delete these branches.

```
$ git branch -d userinput
$ git branch -d bugfix
```

The resulting DAG is

<p align=center>
<img src="img/12b.png?raw=true"
</p>

You've now completed the unix/git tutorial.

At this point, you should understand how to complete all of the problems in the practice quizzes,
and you can use those quizzes to test your understanding of how unix and git works.

<!--
## Exercise

Given the same repo above, draw the DAG that results after running the following commands.
(You do not have to turn in the drawing.)

```
$ echo "everything is awesome" > README
$ git add README
$ git commit -m "changed the README"
$ git checkout -b new_feature
$ touch newfile
$ git add newfile
$ git commit -m 'added newfile'
$ git checkout master
$ touch newfile2
$ git add newfile2
$ git commit -m newfile2
$ cat newfile2
$ ls
$ git merge new_feature
```

**HINT:**
Running `git log --graph` will show an ASCII version of the graph.

You should check the [git cheatsheet](https://github.com/mikeizbicki/ucr-cs100/blob/2015winter/textbook/cheatsheets/git-cheatsheet.md) to figure out what the `git checkout -b` command does.

-->
