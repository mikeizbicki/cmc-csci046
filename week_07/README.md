# week 07: unix shell scripting

<center>
<img src=Strip-Ou-sont-les-tests-unitaires-english650-final.jpg width=400px />
</center>

## Lecture

1. File permissions
    
    1. `ls -l` will list the permissions

    1. `chmod` will change the permissions.
       There are many valid syntaxes for this command.
       See https://www.guru99.com/file-permissions.html for a detailed tutorial.

1. Relative vs Absolute file paths

    1. The root of the computer is called `/`

    1. Any path that starts with a `/` is called an *absolute path*,
       and always refers to the same location on the computer,
       no matter what your working directory is.

    1. Any path that does not start with a `/` is called a *relative path*.
       Relative path is converted to an absolute path by prepending the working directory.
       For example, the relative path `relative/path` as an absolute path is
       ```
       $(pwd)/relative_path
       ```
       The `$(...)` syntax executes the comand within parentheses and replaces it in the string.

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
        1. Bash scripts start with
           ```
           #!/bin/bash
           ```
        1. R scripts start with
           ```
           #!/usr/bin/Rscript
           ```

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
       $ ps -ef | grep username
       ```
       (grep supports arbitrary regex)

       ```
       $ unzip -p /data-fast/geoTwitter-20-01-01.zip | head -n1 | python3 -m json.tool | vim -
       ```

       ```
       $ nohup ./src/map.py --input_path=/data/twitter2020/geoTwitter20-02-16.zip > nohup.geoTwitter20-02-16.zip
       ```
    
1. Signals

    1. `kill` politely requests that a program kill itself.
       It gives the program a chance to save files before ending.
    1. `kill -9` impolitely kills the program without asking first.
       The program has no chance to save files, it just stops.
       Only use this as a last resort when `kill` doesn't work.
    1. `ps` lists running processes created by your current shell
    1. `ps -ef` lists all running processes
    1. `ps -ef | grep username` filters the output of `ps -ef` to only include lines that contain the string `username`
    1. `nohup CMD &` runs the command `CMD` in the background
    1. The ssh server sends `SIGHUP` whenever your shell session disconnects.
       The default behavior of `SIGHUP` is to stop the program,
       but you can use the `nohup` program to block `SIGHUP`.
    1. `CTRL+C` sends `SIGINT` (= signal interupt), which typically stops a program
    1. `CTRL+Z` sends `SIGSTOP` (= signal stop), stops a command
    1. `fg` runs a stopped command in the foreground
    1. `bg` runs a stopped command in the background

1. For loops

<!--
counter / defaultdict in python
serialization / deseialization of unicode
-->

## Lab

Complete the tutorial in [processes.md](processes.md).

Once you've completed the tutorial, submit the string `I've completed the tutorial` to sakai to receive credit.
