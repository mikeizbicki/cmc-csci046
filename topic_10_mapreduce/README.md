# Shell scripting + MapReduce

<center>
<img width=300px src=img/Strip-Ou-sont-les-tests-unitaires-english650-final.jpg />
</center>

**Announcements: Mon 16 Nov**

1. Useful followup classes:

    <img src=https://raw.githubusercontent.com/mikeizbicki/cmc-advising/master/courses-map.png width=100%>


    "Coding" courses:

    1. CS36 Foundations of Data Science
    1. CS143 Big Data: <https://github.com/mikeizbicki/cmc-csci143>

    "Mathy" courses:

    1. CS145 Deep Learning: <https://csci145.rtealwitter.com/>
    1. MATH126 Randomized Algorithms: <https://www.rtealwitter.com/rads2026/>

    <br/>

    <img src=img/math.jpg width=400px />

1. Tim Peters died:
    1. HN discussion: <https://news.ycombinator.com/item?id=50450488>
    1. 2024 writeup about Tim being cancelled from python: <https://chrismcdonough.substack.com/p/the-shameful-defenestration-of-tim>
        1. related-ish: master vs main naming <https://github.com/mikeizbicki/cmc-csci143/issues/750>

1. Electronic quiz material: <https://github.com/mikeizbicki/quiz/blob/master/quiz_shell/topic02_variables_loops.pdf>

1. This week's lab will be posted by end of business today.

## Notes

Shell scripting involves lots of seemingly unrelated concepts.
Once you understand them, you can automate data analysis pipelines and create very complex programs very easily.

1. File permissions
    
    1. `ls -l` will list the permissions

        <img src=img/file_permissions.png width=400px />

    1. `chmod` will change the permissions.
       There are many valid syntaxes for this command.
       See https://www.guru99.com/file-permissions.html for a detailed tutorial.

1. Relative vs Absolute file paths

    1. The root of the computer is called `/`

    1. Any path that starts with a `/` is called an *absolute path*,
       and always refers to the same location on the computer,
       no matter what your working directory is.

    1. On unix, any character except a `/` is valid in a filename.
       (On Windows, there are many more limitations on what is a valid filename.)
       If you have special characters like spaces in a filename, you must escape them or put them in quotation marks.
       For example, the following are equivalent paths:
       ```
       /data/Twitter\ dataset
       '/data/Twitter dataset'
       "/data/Twitter dataset"
       ```

    1. Any path that does not start with a `/` is called a *relative path*.
       Relative path is converted to an absolute path by prepending the working directory.
       For example, the relative path `relative/path` as an absolute path is
       ```
       "$(pwd)/relative/path"
       ```
       The `$(...)` syntax executes the comand within parentheses and replaces it in the string.

    1. Single quotes and double quotes behave the same in python, but differently in the shell.
       Variable substitution is allowed in double quotes but not single quotes.
       The following paths are different:
       ```
       "$(pwd)/relative/path"
       '$(pwd)/relative/path'
       ```

    1. When working on a project, all paths in the project are specified according to the root of the project.
       Therefore, you should always keep yourself in the root folder while working.
       Instead of `cd`ing to other folders, you should just open them directly.

1. Shell scripting

    1. File extensions mean nothing.
       All files are just text files.
       The only difference is how those files are interpreted.

    1. Shebang `#!` tells the computer which program interprets the file

        1. Python scripts start with
           ```
           #!/usr/bin/python3
           ```
        1. POSIX shell scripts start with
           ```
           #!/bin/sh
           ```
        1. Bash scripts start with
           ```
           #!/bin/bash
           ```
           Bash scripts support all the features of the POSIX shell, plus some additional syntax.
           Your default shell on the lambda server is the bash shell.
           There are many other shells that extend the POSIX shell.
           The default on Macs is zsh.
           Windows does not have a POSIX-compliant shell preinstalled.
        1. R scripts start with
           ```
           #!/usr/bin/Rscript
           ```

    1. When executing a script, you must:
        1. have the execute bit set
        1. either:
            1. call it with an absolute path
            1. a relative path that contains a `/`
            1. have the script's directory be located within the `$PATH` environment variable

1. Script arguments
    1. Access the raw arguments in python with
       ```
       import sys
       sys.argv
       ```

    1. Python includes a nice library called argparse which lets you easily build complex command line applications.

    1. Glob patterns `*` are substituted by the shell before being passed to programs.
       The glob `*` is different than the regular expression `*`!

1. Redirection

    1. The pipe `|` connects the output of the program on the left to the input of the program on the right

    1. Input redirection `<` uses the file on the right as input to the program

    1. Output redirection `>` saves the output of a program to a file

    1. Examples:

       ```
       $ ls | wc -l
       ```

       ```
       $ ps -ef | grep username             # grep supports arbitrary regex
       ```

       ```
       $ time unzip -p /data/Twitter\ dataset/geoTwitter20-01-01.zip | wc -l
       ```

       ```
       $ unzip -p /data/Twitter\ dataset/geoTwitter20-01-01.zip | head -n1 | python3 -m json.tool | vim -
       ```

       ```
       $ nohup ./src/map.py --input_path=/data/twitter2020/geoTwitter20-02-16.zip > nohup.geoTwitter20-02-16.zip
       ```
    
1. Signals

    <img src=img/kill.webp width=400px />

    1. `ps` lists running processes created by your current shell
    1. `ps -ef` lists all running processes
    1. `ps -ef | grep username` filters the output of `ps -ef` to only include lines that contain the string `username`
    1. `kill PID` politely requests that program `PID` kill itself.
       It gives the program a chance to save files before ending.
       Technically, `kill` sends `SIGTERM` (= signal terminate).
    1. `kill -9 PID` impolitely kills program `PID` without asking first.
       The program has no chance to save files, it just stops.
       Only use this as a last resort when `kill` doesn't work.
       Technically, `kill -9` sends `SIGKILL` (= signal kill) to the process.
    1. `CTRL+C` sends `SIGINT` (= signal interupt), which typically stops a program
    1. `CTRL+Z` sends `SIGSTOP` (= signal stop), stops a command
    1. `fg` runs a stopped command in the foreground
    1. `bg` runs a stopped command in the background
    1. The ssh server sends `SIGHUP` (= signal hang up) whenever your shell session disconnects.
       The default behavior of `SIGHUP` is to stop the program,
       but you can use the `nohup` program to block `SIGHUP`.
    1. `nohup CMD &` runs the command `CMD` in the background

1. For loops
   
   Reference: https://linuxize.com/post/bash-for-loop/
<!--
counter / defaultdict in python
serialization / deseialization of unicode
-->

## Lab

See <https://github.com/mikeizbicki/lab-coding-agent>.

## Homework

See the instructions in <https://github.com/mikeizbicki/twitter_coronavirus>.

Due: 1 Dec

> **WARNING:**
> The computation can take a long time (potentially many days).
> You will not get an extension for the program not completing in time.
> So I recommend having at least the expensive computations completed before Thanksgiving break.
