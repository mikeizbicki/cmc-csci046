# Customizing your settings

Recall that if you run the command
```
$ ls -a
```
in your home folder, there are many "hidden files".
Because in UNIX hidden files always begin with `.`,
these files are often called "dotfiles".
Dotfiles in the home folder are commonly used to store settings for various programs.

I keep all of my settings archived in a git repo located at <https://github.com/mikeizbicki/dotfiles>.
This ensures that I can easily keep all of my settings consistent between all of the computers that I use.
It also lets me share my settings with you :)

There are four files that will be particularly useful for you in this class:

1. The `.git-prompt.sh` file has tools for working with git.

1. The `.bashrc` file has settings for your bash shell.

1. The `.dircolors` file is not a standard file but something that's included in my `.bashrc` in order to get better coloring in the terminal.

1. The `.vimrc` file has good default settings for vim.

To get these files, we will use the `curl` command.
`curl` takes a url as an input parameter, downloads the url, and prints the result to `stdout`.
For example, to download and view my `.vimrc` file, you can run the command
```
$ curl https://raw.githubusercontent.com/mikeizbicki/dotfiles/master/.vimrc
```

Notice that the `curl` command does not save the file, it only prints it to `stdout`.
This is a common behavior in the UNIX world,
and throughout this course we will see how this behavior lets us chain shell commands together in powerful ways.
For now, in order to save the file,
we will use output redirection with the `>` symbol.
(Recall that output redirection causes anything printed to `stdout` to be saved to a file instead of printed to the terminal.)

Run the following commands in your home folder to download and install the settings files.
(Recall that you can get to your home folder by running `cd` with no arguments.)
```
$ curl https://raw.githubusercontent.com/mikeizbicki/dotfiles/master/.git-prompt.sh > .git-prompt.sh
$ curl https://raw.githubusercontent.com/mikeizbicki/dotfiles/master/.bashrc        > .bashrc
$ curl https://raw.githubusercontent.com/mikeizbicki/dotfiles/master/.vimrc         > .vimrc
$ curl https://raw.githubusercontent.com/mikeizbicki/dotfiles/master/.dircolors     > .dircolors
```
Then logout and login again for the changes to take effect.
You know everything worked if your prompt on the lambda server is green.
