# Object Oriented Programming

This lecture covers how to use classes in Python.
Classes are a tool to help us organize our code more efficiently,
and programs that use classes are said to be *object oriented*.

The material in these videos corresponds to [Section 1.13](https://runestone.academy/runestone/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html) in the textbook,
but it goes into considerably more detail.


1. **Essential.** [Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)

    Notes:

    1. In this video, Corey uses the `pass` keyword when defining classes without explaining its purpose.
       You can review what this keyword does with [this link](https://www.w3schools.com/python/ref_keyword_pass.asp).
    1. Pay close attention to the error message that Python gives when you forget the `self` argument when defining a method.
        It's very easy to forget this argument,
        and so you will get this error message often.
        The error message is also very confusing,
        and so it's not obvious at first what the problem is.
    1. In these videos, Corey assumes that everyone has both a first and last name.
       For most Americans this is true,
       but for people from other cultures this is typically false.
       The famous painter Picaso's full name, for example, is "Pablo Diego José Francisco de Paula Juan Nepomuceno María de los Remedios Cipriano de la Santísima Trinidad Ruiz y Picasso".
       [This article](https://www.w3.org/International/questions/qa-personal-names) by the World Wide Web Consortium (W3C, the organization responsible for standardizing most of the internet) which explains the proper way to handle names in programs,
       and its much more complicated than you think.
       Actually, most things that you think are simple (like time, money, addresses, and distances) are amazingly complex.

       A major source of inequality around the world, right now, is how American programmers make assumptions about these concepts that are unique only to the American experience;
       this prevents other cultures from being able to use or interact with many modern software systems.
       [This github page](https://github.com/kdeldycke/awesome-falsehood) has a curated list of these "falsehoods that programmers believe" about different topics.

    Questions:

    1. What is the difference between a *class* and an *instance*?
    1. What is the difference between an *attribute* and a *variable*?
    1. What is the difference between a *method* and a *function*?
    1. What is the purpose of the `self` argument for methods?
    1. In the code in the video, what is the difference between `Employee.fullname(emp_1)` and `emp_1.fullname()`?
    1. What does the `__init__` function do?
    1. What is a *constructor*?

1. **Essential.** [Python OOP Tutorial 2: Class Variables](https://www.youtube.com/watch?v=BJ-VvGyQxho)

    Notes:

    1. Notice that at timestamp 2:00, Corey forgot to include a `()` on the `emp_1.apply_raise` function call.
       This is a very common error when using class functions and attributes that you are likely to run into in the homeworks.
       But notice that there is no error message displayed,
       instead things just don't work.
       When you are debugging,
       it is good to check that you have parenthesis in the right locations.

    Questions:

    1. What is the difference between a *class variable* and an *instance variable*?
    1. What is the `__dict__` attribute?


1. **Optional.** Decorators.

    The `@` syntax in python is used for special functions called *decorators*.
    Decorators are an example of [metaprogramming](https://en.wikipedia.org/wiki/Metaprogramming),
    which is when you use computer programs to automatically write other computer programs for you.
    This is the ultimate in laziness :)

    For this course, you should be able understand how to use decorators,
    but you are not required to understand exactly how they work under-the-hood.
    For those of you who plan on taking more computer science courses after this, however,
    I strongly recommend you try to learn how they work.
    The following series of video tutorials by Sebastiaan Mathôt provides a great explanation:
    1. [Python Decorators 1: The Basics](https://www.youtube.com/watch?v=PJQ5XopgNog)
    1. [Python Decorators 2: Decorators with arguments](https://www.youtube.com/watch?v=pr1xfd6oTwY)
    1. [Python Decorators 3: Functions to classes](https://www.youtube.com/watch?v=jwcxlZvebDM)

    Questions:
    1. What is a *higher order function*?
    1. What is *syntactic sugar*?
    1. What functionality does the decorator syntax provide sugar for?


1. **Essential.** [Python OOP Tutorial 3: classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)

    Notes:
    1. This video uses an example from the `datetime` library.
       Time is another one of those amazingly complex concepts,
       and so you should ALWAYS use this library whenever you store/manipulate times to ensure that you do it correctly.
       For example, did you know that [some minutes have 61 seconds in them](https://www.timeanddate.com/time/leapseconds.html)?
       that [September 1752 only had 19 days in it](https://www.dawn.com/news/1289505) (in Britain, but not in Spain)?
       and that it's [currently the year 2563 in Thailand](https://en.wikipedia.org/wiki/Date_and_time_notation_in_Thailand)?

    Questions:
    1. What is the difference between a *regular method*, *class method*, and a *static method*?
    1. What is an *alternative constructor*?
       And which type of method is used for alternative constructors?
    1. What is the "giveaway" clue that a regular/class method should be converted into a static method?
    1. When should a method take `cls` as the first argument, and when does it take `self`?
       Are you required to use these names or is it a convention?
    1. Why do class methods name their first argument `cls` instead of `class`?
    1. What does the `weekday` function do in the `datetime` module?


1. **Essential.** [Python OOP Tutorial 4: Inheritance - Creating Subclasses](https://www.youtube.com/watch?v=RSl87lqOXDE)

    Notes:
    1. Corey uses the phase "DRY code" in this video.
       DRY stands for "Don't Repeat Yourself",
       and it's one of the principles programmers follow in order to be more lazy.
       Code that is very repetitive is called WET code because it "Wastes Everyone's Time".
       Programmers who repeat the same code in many places are called WET programmers because their motto is "We Enjoy Typing."
    1. As an example in this video, Corey shows an `HTTPException` class.
       HTTP stands for the *HyperText Transfer Protocol* and is how your webbrowser communicates with webservers.
       It sounds like Corey says this comes from a "whiskey" library,
       but he's actually saying it comes from a "WSGI" library,
       which is a library for generating webpages.
       You can find more details at https://werkzeug.palletsprojects.com/en/1.0.x/ .

    Questions:
    1. What is the difference between a *class*, a *subclass*, and a *superclass*?
       And what is the syntax for each?
    1. What does it mean that a subclass *inherits* the attributes of its *superclass*?
    1. What does the `help` function do?
    1. What does the `super` function do?
    1. What does the `isinstance` function do?
    1. What does the `issubclass` function do?
    1. Why should we not pass `[]` as a default argument to the `__init__` function?
       HINT: Corey doesn't explain this in the video, but we covered this in the memory management homework.

1. **Essential.** [Python OOP Tutorial 5: Special (Magic/Dunder) Methods](https://www.youtube.com/watch?v=3ohzBxoFHAY)

    Notes:
    1. The `timedelta` class is what you get if you subtract two `datetime` instances from each other.
    1. At the end of the video, Corey shows an example using `NotImplemented`.
       It's okay if the purpose of `NotImplemented` doesn't make sense.

    Questions:
    1. How do you identify a special/magic/dunder method?
    1. What is the difference between `__str__` and `__repr__`?
    1. What is operator overloading, and how do you overload the `+` operator?

1. **Optional.** [Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters](https://www.youtube.com/watch?v=jCzT9XFZ5bw)

    Notes:
    1. Personally, I think the use of property decorators is an [anti-pattern](https://stackoverflow.com/questions/980601/what-is-an-anti-pattern),
       and so I recommend not using them.
       But they are commonly used in python,
       and you are likely to encounter them in the real world,
       so it is good to understand how they work at a high level.

    Questions:
    1. When would you use the `@property` decorator?
    1. What is a *getter*?
    1. What is a *setter*?
    1. What is a *deleter*?

