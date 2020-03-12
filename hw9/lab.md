# Lab: shell scripting 

This lab will teach you the shell scripting and command line tools you will need to complete the twitter analysis homework.

Portions of this lab require you to work with a partner.
So you should pair up with another student.
Both of you should complete the lab on your own computers,
but you will have to run certain commands for your partner on your own computer at different steps.

### Creating a shell script

Create a file in your home folder called `script.sh` with the following contents
```
#!/bin/sh

while true; do
    date
    sleep 1
done
```
This is a simple shell script that will print the current time in an infinite loop.
Run the command 
```
$ ls -l script.sh
```
to check the permissions of this file.

### Hacking your partner's account (pt 1)

By default, everyone has read access to everyone else's home folder.
Change your current working directory to be your partner's home folder by running the command
```
$ cd /home/username
```
but replace `username` with your partner's username.
Run
```
$ ls
```
to see all the files in their home folder.
One of those files should be the `script.sh` file they created in the previous step.

Run
```
$ vim script.sh
```
and try to edit the file.
You should get an error message saying that you don't have permissions to edit the file.

Now, have your partner run
```
$ chmod a+w /home/username/script.sh
```
again, where `username` is replaced by their real username.
Now you have write permission on the file,
and you can edit it in vim.

**TASK:**
Change the permissions of your home folder so that other users cannot read the contents of your files.
Note, you should change the permissions of the folder `/home/username` and not the permissions of each individual file.
This will ensure that any new files you create are also hidden.

**NOTE:**
Essentially all hacking boils down to understanding how a computer system is configured differently than the admin of the computer thinks.
Hackers exploit this misconfiguration to their advantage.

### Running the shell file

Return to your home folder by running
```
$ cd
```
Now, try to execute your script by running
```
$ ./script.sh
```
This should fail with a permission denied error message.
That's because we haven't given the file execute permissions yet.

Run the following command to give yourself execute permissions
```
$ chmod u+x shell.sh
```
and then run the file
```
$ ./script.sh
```
Note that the `./` is required. 

This should print the current date/time every second.
You can end the program by pressing `^C`.
(The `^` symbol is the `CTRL` key on your keyboard.
For Mac users, ensure that you are pressing `CTRL` and not `Command`.)

### Background processes

Now restart the program by running 
```
$ ./shell.sh
```
again.
This time, however, press `^Z` to end the process.
This will return you to the command prompt,
but unlike `^C` it does not end the program.
`^Z` temporarily pauses the program,
and you can restart it by running
```
$ fg
``` 
(The `fg` stands for foreground.)
You can pause programs and restart them an arbitrary number of times.

Note that when the process has been paused with `^Z`,
it is not running anymore.
To run the program in the background, enter `bg` (stands for background) instead of `fg`.
Notice that you can still type on the command prompt,
but that `script.sh` is continuing to print out messages while you type.
to end the process,
bring it back to the foreground with the `fg` command,
then press `^C` to terminate the process.

List all the processes running in your current shell with the command 
```
$ ps
```
You should get output that looks like
```
  PID TTY          TIME CMD
62221 pts/1    00:00:00 bash
62359 pts/1    00:00:00 ps
```
although the `PID` values will be different.
Each line corresponds to a process that has been started from your current session.
`bash` is the command interpreter that you are typing commands into,
and `ps` is the command that you just ran.

Now run `./shell.sh`, type `^Z` to pause it, then type `ps` again.
You should now see an additional line in your output corresponding to the `shell.sh` command.
The process id (pid) is how we communicate with processes.
Every time you start a program, a new process is created.
The `PID` column of `ps`'s output will always be unique,
but the other columns may not be.

### Output redirection

Run the following command in your terminal
```
$ ./script.sh > output
```
You should notice that the program is running, 
but no output is being printed to the screen.
You know the program is running because no prompt (`$`) is printed to the screen,
and you can't enter commands.
The `>` symbol is called output redirection,
and sends all of the output of your program into the `output` file.
(`output` can be replaced with any filename you'd like, and is just an example filename.)

After waiting a few seconds, press `^C` to end the program.
Now open the `output` file in vim
```
$ vim output
```
You should see several lines printed out that contain results of running your `./script.sh` file.

You can run this program in the background by running
```
$ ./script.sh > output
```
and then pressing `^Z` to pause the program and then entering
```
$ bg
```
to run it in the background.
Now, the `output` file is being continually written to.
To verify this:
open the file in vim;
check how many lines have been written;
close the file;
reopen the file in vim;
now there should be more lines in the file.

Alternatively, the command `wc -l` shows how many lines are in a file.
Run the command
```
$ wc -l output
```
then wait a few seconds and run the command again.
You should get different numbers both times.

### Killing processes

We've already seen that we can stop the `./shell.sh` command by running the `fg` command and then typing `^C`.
`^C` sends a special signal to a process called `SIGINT`,
and the default response to this signal is to terminate.
Another way to stop the program is by directly killing it with the `kill` command.
`kill` takes a pid as a command line argument,
and you should run 
```
$ kill <PID>
```
where `<PID>` is the pid displayed by the `ps` command of your `./shell.sh` process.
Go ahead and kill the process that you currently have running in the background from the previous section.

### Multiple connections

Create a second connection to the lambda-server. 
Run the command
```
$ ps
```
in both windows and notice that you get different outputs.
The `ps` command by default returns only the processes that were created from your current connection.
To list all processes, run the command
```
$ ps -aux | grep username
```
where `username` is your username.
You should see all the processes created from both of your connected sessions.

Run the command
```
$ ./script.sh
```
in one terminal session;
then in the other, run
```
$ ps -aux | grep username
```

You can see what processes other users are running with the same command.
Just replace `username` with their username instead.

Find the pid of one of your partner's processes and run the `kill` command on it.
You should get a permission denied error.


**NOTE:**
All you *need* to know for this course is how to find the PID of your processes using the command above.
The rest of this section provides more detail about how this command works,
but these details are beyond what is necessary for the Twitter homework.

The vertical bar `|` is called a pipe.
Pipes connect the output of the program on the left to the input of the program on the right.
The `grep` program reads one line at a time from its input and outputs only those lines containing `uesrname`.
To see how this works, run the command
```
$ grep username
```
and start typing some lines.
Notice that if a line does not contain `username` then grep does nothing;
but if the line does contain `username`, then `grep` prints that line.

Any program can be combined with any other program using pipes.
The `find` program, for example, lists all files in the current directory and subdirectory.
(If you run it, you'll probably get a LOT of output!)
You can find only python files by filtering the output of `find` using `grep` like so:
```
$ find | grep 'py$'
```
(The `$` symbol is a [regular expression](https://en.wikipedia.org/wiki/Regular_expression) matching the end of a line;
grep supports arbitrary regular expressions as input.)

The [UNIX Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) is that programs should "Do one thing and do it well."
Then, programs can be combined together using pipes to generate complex behavior.
For example, the `ps` command lists processes running on a system but doesn't provide any filtering.
We combine `ps` with `grep` to filter the output.
In general, whenever we want to filter a program's output, we always combine the previous program with `grep`;
this simplifies all the programs in unix because they do not need to contain code for filtering within them.

### The `HUP` signal

Another way to kill processes is by sending the `HUP` signal.
The `HUP` signal is automatically sent to all children processes of your shell when the connection is closed.
This ensures that you don't accidentally leave thousands of processes running on machines that you're not actively using.

To see how this works,
run the command
```
$ ./shell.sh > output2
```
then type `^Z` and run
```
$ bg
```
to send your shell script to the background.
Verify that this program is running in the background by executing the command
```
$ ps -aux | grep username
```
in the OTHER TERMINAL YOU HAVE OPEN.

Next, close the ssh session that you used to run `shell.sh` by running the command
```
$ exit
```
In your second ssh session (that is still connected),
again run the command
```
$ ps -aux | grep username
```
and notice that your `shell.sh` process is no longer running.
This is because when you closed your ssh connection,
the `HUP` signal was sent to the `shell.sh` process,
ending the process.

### Blocking the `HUP` signal

Sometimes, however, we actually do want to have long running processes that last longer than our current sessions.
To do this, we use the `nohup` command to block the `HUP` signal.

Reconnect a second terminal to the lambda server,
and in this terminal run the command
```
$ nohup ./shell.sh > output2
```
Notice that the only difference between this command and the previous section is the use of the `nohup` command.
Then type `^Z` and run
```
$ bg
```
to send your shell script to the background.
Verify that this program is running in the background by executing the command
```
$ ps -aux | grep username
```
in the OTHER TERMINAL YOU HAVE OPEN.

Next, close the ssh session that you used to run `shell.sh` by running the command
```
$ exit
```
In your second ssh session (that is still connected),
again run the command
```
$ ps -aux | grep username
```
and notice that your `shell.sh` process is still running.
Use the `kill` command to end your `shell.sh` process.

When you launch long-running processes on the lambda-server,
you will have to use the `nohup` command to ensure that they continue to run after you have disconnected.

### The end

You're not required to submit anything for this lab.

<!--
### Hacking your partner (2)

Run
```
$ finger
```
to list all the ssh sessions currently logged in.
Because there is likely to be a lot of users logged into the lambda server right now,
it may be useful to use piping and grep to display only the lines that contain your partner's information:
```
$ finger | grep username
```
This command lists lots of information about each session,
but the important thing for right now is the `Tty` column.

**Historical Note:** `Tty` stands for "teletype", 
which was the original name for a terminal way back in the day when monitors didn't exist and terminal sessions were input on typewriters and output on a printer.
Today, each terminal session has a unique `tty` file.
These are special files located in the `/dev/pts` folder on Linux machines.
By writing to these files, we can write to the different terminals open on the computer;
and by reading from these files, we can read from the different terminals.

Under the `Tty` column of finger's output is a line that looks something like `pts/23`,
(the number `23` will be different for every terminal session).
There is a file in the `/dev/pts` folder that corresponds to your partner's terminal session;
if the finger command shows that their tty is `pts/23`, for example, then the file is `/dev/pts/23`.
Run the following command to 
-->
