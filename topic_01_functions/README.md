# week 01: more git + intermediate python

<center>
<a href="https://xkcd.com/979/">
<img src=wisdom_of_the_ancients.png />
</a>
</center>

## Lecture

1. more git patterns
    1. what if the upstream is updated after we fork?

1. functional programming in python
    1. `map`, `filter`, `lambda`
        1. (optional reference) [realpython](https://realpython.com/python-map-function/)
    1. list comprehensions
        1. (optional reference) [Corey Shafer youtube video](https://www.youtube.com/watch?v=3dt4OGnU5sM)
        1. (optional reference) [realpython](https://realpython.com/list-comprehension-python/)
        1. (optional reference) [python documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

1. memory management in python
    1. local vs global variables
        1. (optional reference) [realpython](https://realpython.com/python-scope-legb-rule/)
    <!--
    1. assignment, copy, and deepcopy
        1. (optional reference) [realpython](https://realpython.com/copying-python-objects/)
    -->

## Lab

**Pre-lab work:**

1. Ensure that you have completed the entire lab for `topic_00` before completing this lab.

1. Spend at least 20 minutes reviewing how to use vim effectively.
    You can either:
    
    1. re-do the vimtutor tutorial from last pre-lab, or
    2. try the more interactive tutorial at <https://www.openvim.com/>.

**Instructions:**

1. In the previous lab, you forked the class repository.
    Since then, however, I have made updates to the class repo,
    and those updates won't be reflected in your forked repo.
    In this first task,
    you must update your forked repo so that it has all the content of my upstream repo.

    Use the following flowchart to help you get the commands correct:

    <img width='100%' src=update_downstream.png />

    Note that the steps with "negative numbers" are events that have already happened,
    steps with "zero numbers" are events that you only have to run once to setup your local repo.
    Every time you need to update your repo,
    you will start with step 1.

1. In this task you will setup the `@p` macro for debugging python programs.

    1. Ensure that you have updated your local git repo with the latest upstream.

    1. `cd` into the `topic_01_functions` folder and then open the file `p_macro` in vim.
       You should see contents that look like
       ```
       ^y$iprint("^[A=", ^[pa)^[^
       ```
       This is the "source code" for the macro,
       and is the sequence of key presses that will be sent to vim whenever you activate the macro.
       The `^[` characters should appear in a slightly different color, and if you move your cursor over them, you'll notice they behave like a single character.
       This is how the `Esc` key gets rendered in the terminal, so each of these characters will cause the `Esc` key to be pressed.

    1. Copy the line into the `p` register by typing the following sequence of commands in normal mode.
       (Ensure that you are in normal mode by pressing `Esc` before typing the commands.)
       ```
       "pyy
       ```
       The `yy` yanks (vim's language for copying) the entire line,
       and the `"p` indicates that we are yanking into the `p` register (vim's language for clipboard).
       Your typical muggle text editor has only a single clipboard to copy/paste from, but vim has a separate register for every key on the keyboard.
       This lets us copy/paste many different things at the same time.
       Macros use the same registers as yanking/pasting, so by yanking into the `p` register we are also creating the `p` macro.
       
    1. To ensure that your macro works, open a new tab with the command
       ```
       :tabe
       ```
       You can use the commands `gt` and `gT` to switch between tabs.

       In your new tab, type
       ```
       python_variable_name
       ```
       into the tab.
       With your cursor anywhere on the line, type `@p` to activate the macro.
       If you've created the macro correctly, you should get the result
       ```
       print("python_variable_name=", python_variable_name)
       ```

    1. (optional) For a detailed reference on writing your own vim macros, see <https://vim.fandom.com/wiki/Macros>.
