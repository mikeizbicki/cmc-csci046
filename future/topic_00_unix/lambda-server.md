# Customizing your bash prompt

I keep all of my settings archived in a git repo located at https://github.com/mikeizbicki/dotfiles .
This ensures that I can easily keep all of my settings consistent between all of the computers that I use.
It also lets me share my settings with you :)

There are three files that will be useful for you in this class:

1. The `.git-prompt.sh` file has tools for working with git,

1. The `.bashrc` file has settings for your bash shell, and

1. The `.vimrc` file has good default settings for vim.

To get these files, we will use the `curl` command.
`curl` takes a url as an input parameter, downloads the url, and prints the result to `stdout`.
For example, to download and view my `.vimrc` file, you can run the command
```
curl https://raw.githubusercontent.com/mikeizbicki/dotfiles/master/.vimrc
```

Notice that the `curl` command does not save the file, it only prints it to `stdout`.
This is a common behavior in the UNIX world,
and throughout this course we will see how this behavior lets us chain shell commands together in powerful ways.
For now, in order to save the file,
we will use output redirection with the `>` symbol.
(Recall that output redirection causes anything printed to `stdout` to be saved to a file instead of printed to the terminal.)

Run the following commands to download and install the settings files:
```
$ curl https://raw.githubusercontent.com/mikeizbicki/dotfiles/master/.git-prompt.sh > .git-prompt.sh
$ curl https://raw.githubusercontent.com/mikeizbicki/dotfiles/master/.bashrc        > .bashrc
$ curl https://raw.githubusercontent.com/mikeizbicki/dotfiles/master/.vimrc         > .vimrc
$ curl https://raw.githubusercontent.com/mikeizbicki/dotfiles/master/.dircolors     > .dircolors
```
Then logout and login again for the changes to take effect.
You know your changes worked if your command prompt is now green.
