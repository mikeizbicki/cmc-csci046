# HTML Validation with Stacks

You will implement an extended version of the balanced parentheses algorithm that checks whether html tags are balanced.
(See [chapter 4.7](https://runestone.academy/runestone/books/published/pythonds/BasicDS/BalancedSymbolsAGeneralCase.html) of the book for details on the balanced parentheses algorithm.)

**Due date:**

Sunday, 16 February at midnight
(you may suggest an alternative due date by submitting a pull request)

**Learning Objectives:**

1. implement the balanced parenthesis algorithm
1. practice using HTML
1. practice using stacks
1. practice using the github/travis toolchain

## Background

HTML is how webpages format their content.
A simple example is the following code:

```
Data structures is <strong>the best</strong>!
```

Which results in text that looks like: Data structures is <strong>the best</strong>!

The text between angle brackets is called a tag,
and tags always come in pairs.
The first tag (`<strong>`) is called an opening tag and the second tag (`</strong>`) is called a closing tag.
Closing tags always have the same text as an opening tag, except that a slash `/` is added at the very beginning.

There are many html tags that control different formatting options,
and they get combined in complex ways to generate the layout of webpages.
For example, the `<em>` tag causes text to be italicized and the `<u>` tag causes text to be underlined.
The HTML:

```
<u>Data structures</u> is <strong>the <em>best</em></strong>!
```

results in text that looks like: <u>Data structures</u> is <strong>the <em>best</em></strong>!

Large webpages have tens of thousands of html tags in a single file,
and it is important to verify that this html is correct.
Examples of incorrect html are:

1. `<strong>example` (there is no closing `</strong>` tag)
1. `<strong>python <u>is </strong> awesome </u>` (the `</strong>` closing tag needs to be outside of the `</u>` tag)

The goal of this assignment is to write a program which can detect these HTML errors.

**Real World Application:**
The [World Wide Web Consortium (W3C)](https://w3.org) is the organization responsible for maintaining the HTML standard.
They have a program online at https://validator.w3.org/ which performs HTML validation,
and it is used by web developers around the world to improve their webpages.
You are implementing a limited version of this program.

## Tasks

Complete the following tasks:

1. Fork the [html\_validator repo](https://github.com/mikeizbicki/html_validator) and enable travis
1. Update the `README.md` file so that the travis button points to your repo
1. Implement the `validate_html` and `_extract_tags` functions so that all test cases in `tests/test_main.py` pass

Your grade will be the percentage of test cases that successfully pass in travis.

### Extra Credit

You can earn 10% extra credit on this assignment by making your code pass additional test cases specified in `tests/test_ec.py`.
These test cases check more possible html errors that the original set of test cases do not cover.

If you choose to do the extra credit, you must enable the additional test cases in travis by uncommenting the line

```
#  - python3 -m pytest -v tests/test_ec.py
```

## Submission

Submit the link to your forked repository on sakai.

## Collaboration Policy

**You are not allowed to look at another student's github repo.**

All other forms of collaboration with other students are encouraged.
You may use any other online resources you like to complete this assignment.
