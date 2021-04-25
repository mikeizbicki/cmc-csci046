# Week 13: Graphs

Notes to be added.

## Homework

You will create a pypi package containing all of your code from your `tree` repo.

**Learning Objectives:**

1. understand package management systems
1. create a real python package that anyone in the world can download

### Background

The [Python Package Index (PyPI)](https://pypi.org/) is a central repository for all python software.
Whenever you run a command like
```
$ pip3 install XXX
```
your computer downloads the `XXX` package from pypi. 

### Tasks

Complete the following tasks:

1. Checkout your `master` branch.

1. Merge the following branches into `master`: `unicode` and `heap`.
   
   1. This will ensure that you get all of the code from all of your branches.
      You should make sure you understand why merging only these two branches will get you all of the code you've written.

1. Create a file called `LICENSE` that contains the text of any open source license of your choosing.

    1. The `LICENSE` file describes how other people can use your code.  If a repo does not have a `LICENSE` file, you cannot legally (in the US and most other countries) use that code for any purpose without explicitly asking permission from the author.
    1. An "open source license" is a license that satisfies two criteria:
        1. Anyone can use the software for any purpose
        1. The source code is provided with the software
    1. Examples:
        1. BSD3/MIT: no additional conditions (in particular, no condition that you must distribute any modifications)
        1. GPL: if someone modifies the source code and *distributes the modified software*, they must also distribute the modified source code
        1. AGPL: if someone modifies the source code and *allows users to connect to the modified software (e.g. via a webpage)*, they must also distribute the modified source code
        1. And many more... big projects often create their own licenses
            1. Python uses the Python Software Foundation (PSF)
            1. Firefox uses the Mozilla Public License (MPL)
    1. GPL-style licenses are sometimes called "copyleft"
    1. Non-examples:
        1. Proprietary software: Windows can be used for any purpose (pass condition 1), but Microsoft does not distribute the source code (fail condition 2)
        1. MongoDB/ElasticSearch's SSI license provides the source to the software (pass condition 2), but disallows cloud hosing companies like Amazon to provide the software to their customers (fail condition 1)
    1. You can find a copy of the license files, and guidelines on which license to pick, at https://choosealicense.com/ .

1. Follow [this tutorial](https://realpython.com/pypi-publish-python-package/#preparing-your-package-for-publication) in order to create a `setup.py` file and upload your project to pypi.
    You must update the configuration settings correctly, and you must choose a project name that begins with `cmc_csci046_`.

1. Submit two links to sakai:

    1. the link to your project on pypi

    1. the link to your github repo
