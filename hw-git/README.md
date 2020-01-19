# using git and github

**Learning Objectives:**

1. learn how to use the git version control system
1. learn how to work on a remote unix server

## background

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

### creating your first repo (and some basic unix commands)

Create a folder named `firstrepo` and `cd` into it:

```
$ mkdir firstrepo
$ cd firstrepo
```

This folder will be the home of your first git repository.
Run the following command to initialize it:

```
$ git init
Initialized empty Git repository in /home/mizbicki/tmp/firstrepo/.git/
```

All the information for the git repository is stored in a hidden folder called `.git`.
The folder is hidden because it begins with a `.`.
By default, the `ls` command does not display these hidden folders.
To display them, you must pass the `-a` flag.
Compare the results of the following two commands:

```
$ ls
$ ls -a
.  ..  .git
```

Now we are ready to add some files into our repo.
Every repo in this class must have a `README` file.
Create the file using the following command:

```
$ touch README
```

The `touch` command is a standard unix command.
If the input file does not already exist, `touch` creates an empty file with that name.
If the file does already exist, it updates the file's timestamp to the current time.
The `ls -l` command displays the full information about each file in the current directory.
Run the following commands:

```
$ ls -l
$ touch README
$ ls -l
```

Notice how the timestamp in the first `ls` is different than the timestamp in the second `ls`.

We've created our first file, but git doesn't know about it yet.
Run the command:

```
$ git status
```

In the output, there is a section labeled "untracked files."
Notice that the `README` file is in this section.
We need to add it into our project using the command:

```
$ git add README
```

Now, when we run `git status`, there is a section labeled "Changes to be committed" with the `README` file underneath it.

Whenever we finish a task in our repo, we "commit" our changes.
This tells git to save the state of the repo so that we can come back to it later if we need to.
Commit your changes using the command:

```
$ git commit -m "my first commit"
```

Every commit needs a "commit message" that describes what changes we made in the repo.
Writing clear, succinct, informative commit messages is one of the keys to using git effectively.
In this case, we passed the `-m` flag to git, so the commit message was specified in the command line.
If we did not pass a flag, then git would have opened the vim editor for us to type a longer commit message.
Whether or not you use the `-m` flag is purely a matter of style, but in my experience, it's usually easier to add the flag.

Let's add some actual code to our project.
Create a file `main.py` with the following code:

```
#!/usr/bin/env python3

print("hello world")
```

**NOTE:**
The first line in the file above is called the shebang.
For our purposes, you don't need to understand this line at this point.
See [this stackoverflow question](https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take) for more details.

Now run your program:

```
$ python3 main.py
```

Then add it to the repo and commit your changes:

```
$ git add main.py
$ git commit -m "added the first code"
```

Let's make one more commit so we'll have something to play with.
Run the command:

```
$ echo "This program prints \"hello git\"" > README
```

Remember that `echo` prints to `stdout` and the `>` does output redirection.
So this command changes the contents of the `README` file.

The command `cat` prints the contents of a file to `stdout`.
Verify that your `README` file has changed using the command:

```
$ cat README
```

Now run:

```
$ git commit -m "modified the README"
```

Uh oh!

We got an error message saying that ends with `no changes added to the commit`.

Every time you modify a file, if you want that file included in the commit,
you must explicitly tell git to add the file again.
This is because sometimes programmers want to commit only some of the modified files.
We can commit the changes by:

```
$ git add README
$ git commit -m "modified the README"
```

### traveling through time

Okay!

Now we're ready to take advantage of git's power.

Run the command:

```
$ git log
```

This gives us a history of all our commits.
For each commit, there are four pieces of information.
The first is the commit identifier.
This is a long hexadecimal sequence, for example: `093d5fa3c60ce204b6ddba86d4f9c355b4856f10`.
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
For me, the hash of "my first commit" is `a20aef2096d98ab53d1495f823409e2cc8cd54b9`.
So to inspect that commit, I would run:

*(You should replace the hash below with the hash of your "my first commit")*

```
$ git checkout a20aef2096d98ab53d1495f823409e2cc8cd54b9
```

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

Your `main.py` file disappeared!
All of the files tracked by git have returned to their previous state.

Let's restore all those changes.  Run the command:

```
$ git checkout master
```

And verify that our changes have been restored:

```
$ cat README
$ ls -l
```

### git repos are trees

Another important use of version control systems is working with multiple versions of the same project at once.
This is VERY useful.
Also, you'll be required to do this in future homework assignments (and all throughout your illustrious careers), so pay attention!

Every version of our repo is called a "branch."
A project can have many branches, and every branch can be completely different than every other branch.
List the branches in your current project using the command:

```
$ git branch
```

This should list just a single branch called `master`.
This branch was created for you automatically when you ran the `git init` command.

One way to think of branches is as a nice label for your commit hashes.
Your "master" branch currently points to your commit with the message "modified the README."
That's why when we ran `git checkout master` above, it restored our project to the state of that commit.
We could also have used `git checkout [hash]`, if you replaced `[hash]` with the appropriate hash value.
But that's much less convenient.
When you use `git checkout` in the future, you will usually be using it on branch names.

From now on, we'll be drawing pictures of our git repos so you can visualize what's going on.
Currently, our repo looks like:

<p align=center>
<img src="images/3.png?raw=true">
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

Our repo tree now looks like:

<p align=center>
<img src="images/4.png?raw=true">
</p>

Switch to our new branch using the command:

```
$ git checkout userinput
```

Now run:

```
$ git branch
```

and verify that the asterisk is next to the `userinput` branch.
Since the only thing you did was switch branches, the repo tree looks almost the same.
The only difference is the asterisk has moved.

<p align=center>
<img src="images/5.png?raw=true">
</p>

Let's modify our `main.py` file so that it asks the user their name before saying hello:

```
#!/usr/bin/env python3

print('enter your name')
name = input()
print(f'hello {name}')
```

**NOTE:**
The code above uses python f-strings,
which is a new feature added into python 3.6.
Whenever a string literal begins with `f'`,
any values within curly braces will be substituted into the string.
See [this tutorial](https://cito.github.io/blog/f-strings/) if you want to learn more.

We commit our changes to the current working branch the same way we committed them before:

```
$ git add main.py
$ git commit -m "added user input"
```

Before this commit, the `userinput` and `master` branches were pointing to the same commit.
When you run this command, the `userinput` branch gets updated to point to this new commit.
Now your tree looks like:

<p align=center>
<img src="images/6.png?raw=true">
</p>

Let's verify that our changes affected only the userinput branch and not the master branch by running the following commands:

```
$ git checkout master
$ cat main.py
$ git checkout userinput
$ cat main.py
```

Notice that the contents of `main.py` are different depending on which branch you are on.

We're not done with this feature yet.
Whenever you add a feature, you also have to update the documentation!

Update the `README` file with the command:

```
$ echo "This program asks the user for their name, then says hello." > README
```

And add it to the repo:

```
$ git add README
$ git commit -m "updated README"
```

Your repo tree now looks like:

<p align=center>
<img src="images/7.png?raw=true">
</p>

The way branches are used out in the real world depends on the company you work for and the product you're building.
A typical software engineer might make anywhere from one new branch per week to 5 or more new branches per day.

### fixing a bug

Wait!

While we were working on our `userinput` branch, someone reported a bug in our `master` branch.
In particular, the main function in our master branch returns 1, but a successful program should return 0.  In UNIX, any return value other than 0 indicates that some sort of error occurred.

To fix this bug, we first checkout our master branch:

```
$ git checkout master
```

Then create a `bugfix` branch and check it out:

```
$ git branch bugfix
$ git checkout bugfix
```

Here's the tree.
Notice that the `bugfix` branch starts where the `master` branch was because we switched to `master` before creating `bugfix`.

<p align=center>
<img src="images/8.png?raw=true">
</p>

Now we're ready to edit the code.  Update the `main` function to return 0, then commit your changes:

```
$ git add main.cpp
$ git commit -m "fixed the return 1 bug"
```

Since you made the commit on the `bugfix` branch, your tree splits off in another direction and now looks like this:

<p align=center>
<img src="images/9.png?raw=true">
</p>

### merging branches

We want our users to get access to the fixed software, so we have to add our `bugfix` code into the `master` branch.
This process is called "merging."

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

Your tree will now look like this:

<p align=center>
<img src="images/10.png?raw=true">
</p>

Using branches like this to patch bugs is an extremely common usage pattern.
Whether you're developing open source software or working on facebook's user interface,
this is the same basic procedure you will follow.

With real bugs on more complicated software, bug fixes won't be quite this easy.
They might require editing several different files and many commits.
It might take us weeks just to find out what's even causing the bug!
By putting our changes in a separate branch, we make it easy to have someone fixing the bug while someone else is adding new features.

### merge conflicts

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
Auto-merging main.cpp
CONFLICT (content): Merge conflict in main.cpp
Automatic merge failed; fix conflicts and then commit the result.
```

This error is called a "merge conflict" and is one of the hardest concepts for new git users to understand.
Why did this happen?

In our `bugfix` branch above, git automatically merged the `main.cpp` file for us.
It could do this because the `main.cpp` file in the `master` branch did not change after we created the `bugfix` branch.
Unfortunately, after we merged the `bugfix` branch into master, this changed the `main.cpp` file.
Now when git tries to merge our changes from the `userinput` branch, it doesn't know which parts to keep from `userinput`, and which parts to keep from `bugfix`.
We have to tell git how to do this manually.

If you inspect the contents of the `main.cpp` file, you'll see something like:

```
#include <iostream>
#include <string>

int main()
{
<<<<<<< HEAD
    std::cout << "hello git!" << std::endl;
    return 1;
=======
    std::string name;
    std::cout << "What is your name?" << std::endl;
    std::cin >> name;
    std:::cout << "Hello " << name << "!" << std::endl;

    return 0;
>>>>>>> userinput
}
```

As you can see, the file is divided into several sections.
Any line not between the `<<<<<<<<` and `>>>>>>>>` lines is common to both versions of `main.cpp`.
The lines between `<<<<<<<< HEAD` and `=======` belong only to the version in the `master` branch.
And the lines between `=======` and `>>>>>>>> userinput` belong only to the `userinput` branch.

The key to solving a merge conflict is to edit the lines between `<<<<<<<` and `>>>>>>>` to include only the correct information from each branch.
In our case, we want the `return` statement from the `master` branch,
and all of the input/output from the `userinput` branch.
So we should modify the `main.cpp` file to be:

```
#include <iostream>
#include <string>

int main()
{
    std::string name;
    std::cout << "What is your name?" << std::endl;
    std::cin >> name;
    std::cout << "Hello " << name << "!" << std::endl;

    return 0;
}
```

Once we have resolved this merge conflict, we can finalize our merge.
We first tell git that we've solved the conflict by adding the conflicting files,
then we perform a standard commit:

```
$ git add main.cpp
$ git commit -m "solved merge conflict between userinput and master branches"
```

And your tree looks like:

<p align=center>
<img src="images/11.png?raw=true"
</p>

As you can see, resolving merge conflicts is a tedious process.
Most projects try to avoid merge conflicts as much as possible.
A simple strategy for doing this is using many small source files rather than a few large files.
Of course, in most projects merge conflicts will be inevitable.
That's just the reality of working on large projects with many team members.

### exercise

Given the same repo above, draw the tree that results after running the following commands.
You will have to submit this to the TA before the end of lab.

```
$ git branch -d userinput
$ git branch -d bugfix
$ echo "everything is awesome" > README
$ git add README
$ git commit -m "changed the README"
```

You should check the [git cheatsheet](https://github.com/mikeizbicki/ucr-cs100/blob/2015winter/textbook/cheatsheets/git-cheatsheet.md) to figure out what the `git branch -d` command does.

### Enrollment and advanced tutorial

You should also go through the more advanced git exercises. [Advanced](Advanced.md)

It may help during this class when managing your class programs.

When you are done with that you will still need to enroll in the class. [Enrollment](Enrolling.md)


