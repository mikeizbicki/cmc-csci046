
# simplest possible class
# customary to have class names capitalized
#
# in python, we call classes "first class objects";
# this means that we can use and reference classes just like any other object/variable
class Duck:

    # this is not allowed in python
    #weight = 0
    #height = 2
    #name = 3

    # called the constructor of a class
    # is called a "double underscore" / "dunder" method ; "magic" method
    def __init__(self, weight=None, height=None, name=None):
        self._weight = weight
        self._height = height
        self._name = name

    # repr stands for "representation" and should be a computer readable representation of the information in the class
    # we don't print it to the screen, instead we return a string
    def __repr__(self):
        return 'Duck(weight='+str(self._weight)+',height='+str(self._height)+',name='+self._name+')'

    # all "member functions" / "methods" typically take "self" as the first parameter
    def quack(self):
        print('quack... my name is ' + self._name + '... quack')

# classes give us a way to group things that are "logically related" together
# standard attributes:
# - name
# - height
# - weight
# standard functions that we want

# variables "inside" a class == variables appearing to the right of a . are called "attributes"


class Dog:
    # all memeber variables have public scope
    # other programming languages have what we call "private" scope as well
    # if we add an _ in front of a variable, it means you "shouldn't" access it 
    def __init__(self):
        self.height=1
        self.weight=50
        self._name = 'Lassie'

    def bark(self):
        print('bark... my name is '+self.name+'... bark!')

lassie = Dog()
donald = Duck(name='donald')
daisy = Duck(5, 10, 'daisy')

ducks = [donald, daisy]

# we can convert lassie into a duck by teaching it how to quack

def quack_new(self):
    self.bark()
lassie.quack = Duck.quack

#lassie.quack()

for duck in ducks:
    duck.quack()
