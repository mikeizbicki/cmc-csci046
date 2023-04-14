# Lab: Deploying

In this lab, you will go through the steps of deploying your containers library so that it is publicly available for everyone to use.
Probably no one will actually want to use this particular package,
but it will learn about:

1. what the `pip install` command actually does under the hood,
1. open source licenses,
1. and recent controversies in the open source community.

<!-- FIXME: add
1. security problems associated with `pip`,
-->

> **NOTE:**
> If you didn't pass all the test cases for all of the assignments, don't worry.
> You can still get full credit on this lab.

### Tasks

**Task 0: Merging into the master branch**

In the containers repo, checkout your `master` branch.
Then run
```
$ git merge bst
```
to merge all of the code from the bst branch into the master branch.
Resolve any merge conflicts by:
1. running `git status` to view which files the conflict is happening inside of,
1. fixing the files with `vim`,
1. then adding/committing the files with git.
Finally, verify that code continues to work correctly by running pytest.

<!--
> **NOTE:**
> You will have to have green badges for all 
-->

> **RECALL:**
> Anytime that a programmer is developing a new feature for a software project,
> they do that inside of a branch.
> Then, when the feature is ready (e.g. passing all of the test cases),
> that branch is merged into master.
> We generally never work directly in the master branch.
> We want the master branch to be "production ready code" that can always be downloaded and installed immediately.
> Whenever you accept a "pull request" on github,
> github performs all of these steps above automatically.
> If github actions is enabled, it will also tell you whether the test cases are still passing.

Repeat the above steps for all of the branches in your project.

**Task 1: Pushing to github**

We generally do not want github to contain out of date branches that we are no longer working on.
Therefore, we need to delete all of our non-master branches from github.
We do this using the command
```
$ git push <remote> -d <branchname>
```
where `<remote>` is the name of the remote you are working with (probably `origin` for you),
`<branchname>` is the branch you are trying to delete,
and `-d` indicates that we should be deleting the branch instead of doing a normal push to the branch.

> **WARNING:**
> Once the branch is deleted, there is no way to recover it.

Once you are confident that everything has been correctly merged into master,
push your master branch to github and delete all of the other non-master branches.

> **WARNING:**
> You must have exactly one branch deployed on github to get full credit for this assignment.
> If there are more than one branch, you will lose 1 point/branch.

**Task 2: Selecting a license**

By default, code published on github is NOT open source,
even if it is publicly available for other people to read and download.
In order to make a project open source, you need to apply an open source license to the file.
It is convention to create a file `LICENSE` in the root folder of your project that contains this license information.
If a repo does not have a `LICENSE` file, you cannot legally (in the US and most other countries) use that code for any purpose without explicitly asking permission from the author.

Technically, an "open source license" is a license that satisfies two criteria:
1. Anyone can use the software for any purpose.
1. The source code is provided with the software.

Examples of open source licenses include
1. BSD/MIT: no additional conditions (in particular, no condition that you must distribute any modifications)

    > **ASIDE:**
    > BSD stands for the Berkeley System Development license and was developed by Berkeley.
    > There is no meaningful difference between these licenses.
    > Historically, there has been a large east coast/west coast split in computer science,
    > and west coasters would use the BSD license,
    > while east coasters would use the MIT license.

1. GPL: if someone modifies the source code and *distributes the modified software*, they must also distribute the modified source code (licenses like the GPL that require redistribution are often called "copyleft" licenses)
1. AGPL: if someone modifies the source code and *allows users to connect to the modified software (e.g. via a webpage)*, they must also distribute the modified source code
1. And many more... big projects often create their own licenses
    1. Python uses the Python Software Foundation (PSF)
    1. Firefox uses the Mozilla Public License (MPL)

There are many licenses, however, that are not open source.
For example:
1. Proprietary software: Windows can be used for any purpose (pass condition 1), but Microsoft does not distribute the source code (fail condition 2)
1. The [JSON license](http://www.json.org/license.html) (recall that JSON is the data format used to store the tweet datasets), states that
    > The Software shall be used for Good, not Evil.
    And so JSON is technically not open source (fails condition 1) even though anyone is allowed to use JSON (passes condition 2).
1. While the JSON license is amusing, a more serious example is the SSI license used by MongoDB and ElasticSearch.
    These are two database companies with multi-billion dollar market valuations.
    Their license provides the source code of the software to everyone in the world for free(pass condition 2),
    but disallows cloud hosing companies like Amazon to provide the software to their customers (fail condition 1).

> **ASIDE:**
> There has been a lot of recent legal controversy in the software engineering world over GitHub copilot and software licenses.
> [Copilot](https://github.com/features/copilot) is a ChatGPT-like tool that software developers can use to have AI partially write their code.
> Copilot [was trained on all code stored on github](https://news.ycombinator.com/item?id=27769440),
> even if that code was not under a license that explicitly allows for reuse of the code
> (and even if the code was under a license that explicitly disallows AI training).
> The legality of GitHub's actions here has not yet been tested in court.

For this task, you must select an open source license (I recommend either GPL or BSD depending on your politics)
and include the appropriate `LICENSE` file in your project.
The `LICENSE` file must contain the actual text of the license,
and not just a statement about which license you are using.
You can find a copy of the license files at <https://choosealicense.com/>.
After you have created your `LICENSE` file,
push it to github.

**Task 3: the `master` vs `main` branches**

I first created the containers assignment in 2019.
At that time, all git projects used `master` as the default branch name.
On [01 October 2020, github deployed a change making `main` the default branch name instead of `master`](https://github.blog/changelog/2020-10-01-the-default-branch-for-newly-created-repositories-is-now-main/) on github.
[This article from zdnet explains the motivation in detail](https://www.zdnet.com/article/github-to-replace-master-with-alternative-term-to-avoid-slavery-references/),
but the basic idea is that the name master could be offensive to black people because it is a reminder of slavery.
By removing this reference, github hoped to make the programming community more inclusive.

GitHub's switch from `master` to `main` has been highly controversial.
A very famous rant (by a black software developer) titled [Github f\*ck your name change](https://mooseyanon.medium.com/github-f-ck-your-name-change-de599033bbbe)
argues that this name change trivializes the black lives matter movement
and actively harms beginner developers by complicating the ecosystem.
(I recommend looking through the [corresponding hacker news post](https://news.ycombinator.com/item?id=26487854) to get an idea of how the community reacted.)
One of the primary arguments against the name change is that this would break lots of software.
And this did end up happening.
For example, the [reddit website went down for several hours because of a confusion between `master` and `main` branches](https://old.reddit.com/r/RedditEng/comments/11xx5o0/you_broke_reddit_the_piday_outage/).

For this class, I don't care about your opinion on the `master` vs `main` controversy.
If you would prefer to have a `main` branch because you feel it is more inclusive,
then you can [follow github's official directions for migrating](https://github.com/github/renaming#renaming-existing-branches).
If you are worried, however, that this might break something and don't want to perform the migration,
then you are not required to.

**Task 4: Deploying to pypi**

The [Python Package Index (PyPI)](https://pypi.org/) is a central repository for all python software.
Whenever you run a command like
```
$ pip3 install XXX
```
your computer downloads the `XXX` package from pypi. 

Follow [this tutorial](https://realpython.com/pypi-publish-python-package/#preparing-your-package-for-publication) in order to create a `setup.py` file and upload your project to pypi.
You must update the configuration settings correctly, and you must choose a project name that begins with `cmc_csci046_`.
You should verify that your project uploaded correctly by running
```
$ pip3 install <your_project_name>
$ python3
>>> import containers
```
and verifying that the containers library loaded correctly.

## Submission

Submit two links to sakai:
1. the link to your project on pypi
1. the link to your github repo
