# Week 09: Unicode

Today (Mar 31) is [César Chávez Day](https://en.wikipedia.org/wiki/Cesar_Chavez_Day),
which commemorates the labor movement of primarily migrant Latino farm workers in California.
In order to observe the holiday, we will discuss how to properly handle Spanish (and all non-English) words and names inside Python.

1. Unicode
    
    1. A system for representing *every* possible language using computers

       1. developed by thousands of phd-level linguists and computer scientists from around the world

       1. replaces older language/country-specific systems

          1. ASCII - English/US
          1. KOI8 - Russian/USSR

       1. also used for emoji

          <center>
          <img width='80%' src=vomiting_emoji.png />
          </center>

          You can find an explanation of this comic at https://www.explainxkcd.com/wiki/index.php/1813:_Vomiting_Emoji

       1. Python was essentially the first language with good native Unicode support,
          which helped drive its initial popularity.

       1. The split between python 2 and 3 is basically over how to handle unicode.
          
          1. Python 3 chooses what's best for pure-python developers.

          1. Pytohn 2 chooses what's best for people who combine python with other languages (especially C).

    1. Key definitions:

        1. code point: a number associated with a particular character

        1. font: a mapping from a code point to an image
            1. fonts are chosen by the device, and can completely change the meaning of the underlying string

            1. Apple decided to change te meaning of the gun emoji: https://blog.emojipedia.org/apple-and-the-gun-emoji/

        1. combining character: a character that modifies the preceding character

        1. normal forms: there are many ways to represent the same string in unicode, and a "normal form" is a canonical way to represent a string

            1. normal form composed (NFC): remove as many combining characters as possible

            1. normal form decomposed (NFD): use as many combining characters as possible

    1. References:
        1. Joel Spolsky's [the absolute minimum every software developer absolutely positively must know about unicode (no excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

        1. NSA's security risks of Unicode: https://apps.nsa.gov/iaarchive/library/reports/unicode-security-risks.cfm

## Homework/lab instructions

There is no separate graded lab for this week.
We will still have lab, and it will be a chance for everyone to work/ask questions.

1. The https://github.com/mikeizbicki/containers repo has a new branch called `unicode`.
   This branch contains the homework for this week.

1. You should:

    1. Create and checkout a branch in your homework repo called `unicode`.

    1. Pull the contents of my `unicode` branch into your branch.

    1. Fix the file `containers/unicode.py` so that all the test cases pass.

    1. Update your `README.md` file so that the build status icons point to your repo.

    1. **IMPORTANT:**
       All your work must be done in the `unicode` branch,
       and **you must not merge your work into the `master` branch**.
       If you merge your work into `master`, you will receive -2 points on the assignment.

1. Submit the link to your `unicode` branch on github to sakai.
   If you submit a link to your master branch instead, you will receive -2 points on the assignment.
