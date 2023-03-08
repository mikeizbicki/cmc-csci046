# Topic 07: Binary Search Trees (BSTs) / Recursive Data Structures

## Announcements

1. Grades updated in sakai

    <img src=grades.png />

    1. Contact me if there are mistakes
    1. I'm very proud of you all
        1. Other professors complain my grades are "too high"
        1. I believe this is a result of:
            1. clear and objective grading criteria
            1. interesting assignments that prepare you for realworld jobs + technical interviews
           <!--
           Message from Guido:
           ===================
           You guys rock!
           This is *really* hard stuff you're learning.
           Sorry I couldn't make python any simpler.
           At least you can't "blame" me for your git problems!
           Anyways, you'll all be using this stuff everyday in industry.
           So keep up the good work!
           -->
    1. [Google's VP in charge of hiring people says "GPA’s are worthless as a criteria for hiring, and test scores are worthless" because they don’t predict how productive an employee will be.](https://www.nytimes.com/2014/02/23/opinion/sunday/friedman-how-to-get-a-job-at-google.html)
    1. Lots of "culture fit" interview stuff not in your grade:
        1. How well do you use your tools (e.g. vim shortcuts)
        1. Do you use markdown formatting correctly (e.g. reporting error messages with code blocks vs inline code)
        1. Do you pronounce things correctly (e.g. deque, OOP)
        1. Do you address people properly (e.g. Mike, not professor)

1. Next 3 homeworks:

    1. They will all have special instructions using the same containers repo

    1. More involved than previous assignments, and they all build off of each other

    1. First homework easiest (worth 32 points)
    
        second homework hardest (worth 32 points)
        
        third homework in the middle (worth 64 points, no collaboration allowed)

1. Modified due dates because of spring break:
    1. This week's lab due Sunday 19 Mar
    1. This week's homework due Tuesday 21 Mar

## Lecture

<img width=600px src=cgxof0jkru551.png />

<!--
<img src=l5nus3752l261.png />
-->

1. Recursive data structures
    1. No assignments on "linear" data structures.
        These are all in your quiz on OOP 2.

        They are common for "easy" technical interview questions,
        but they are never actually implemented in python.

        They are discussed in the textbook,
        and some good review videos are:

        1. [singly linked lists](https://www.youtube.com/watch?v=FSsriWQ0qYE&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=5)
        1. [circular linked lists](https://www.youtube.com/watch?v=5WoNhm7sOnA&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=19)
        1. [doubly linked lists](https://www.youtube.com/watch?v=8kptHdreaTA&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=24)
    1. You will have assignments on:
        1. binary trees (containers 1, 2, 3)
        1. binary search trees (containers 1)
        1. AVL trees (containers 2)
        1. Heap trees (containers 3)

1. 3 algorithms on binary trees:
    1. traversals
        1. pre-order
        1. in-order
        1. post-order
    1. height
    1. size

1. 3 algorithms on binary search trees:
    1. find
    2. insert
    3. delete

1. WET vs DRY programming
    1. WET: wastes everyone's time / we enjoy typing
    1. DRY: don't repeat yourself

        OOP / class inheritence is a tool for "keeping your code DRY"

        <img src=keep-my-diaper-and-my-code-dry.jpg width=300px />

1. Motivation:
    1. Binary search lets us check whether an element is in a sorted list in O(log n) time,
       but adding new elements to the sorted list takes O(n) time.

    1. Binary search trees (BSTs) let us perform both insertion and deletion in O(log n) time.

        1. The "right" way to think of them is as a combination of sorting and binary search algorithms merged together in one.
    
        1. Technically, the BST doesn't guarantee worst case runtimes of O(log n) time.

        1. It guarantees that the works case runtimes are O(height), and the height is O(n) in the worst case.

        1. Next week, we will extend the BST to the AVL tree, which guarantees the height is O(log n).

    1. The downside of BSTs is that their implementations will get very complicated.
       Fortunately, they only need to be implemented once, then everyone else can use them.

1. Reference:
    1. [Textbook](https://runestone.academy/runestone/books/published/pythonds/index.html) Sections 7.1-7.7, 7.11-1.14

        The textbook has a working implementation of a binary search tree that you can base your implementation on.
        The main difference is that they are implementing a "Dictionary/Map" interface (i.e. associate keys with values),
        and we are implmementing a "set" interface (only check if keys are contained in the tree, without associating with a value).
        The set is a bit simpler because there are fewer values to keep track of.
        We are focusing on the set implementation mainly so you can't just "copy/paste" their solutions and have to reimplement everything from scratch.
        You can definitely use their implementation as a guide, however.

## Lab

TBA

## Homework instructions

1. The <https://github.com/mikeizbicki/containers> repo has a new branch called `bst`.
   This branch contains the homework for this week.

1. You should:

    1. Create and checkout a branch in your homework repo called `bst`.

    1. Pull the contents of my `bst` branch into your branch.

        > **IMPORTANT:**
        > All of your work for this assignment must be contained in the `bst` branch of your repo,
        > and the `master` branch must remain unchanged.
        > If your master branch is modified in any way,
        > you will receie a -8 point penalty on this assignment.

    1. Fix the file `containers/BinaryTree.py` and `containers/BST.py` so that all the test cases pass.

1. Submit the link to your `bst` branch on github to sakai.
   If you submit a link to any other branch instead,
   you will receive a -4 point penalty on the assignment.
