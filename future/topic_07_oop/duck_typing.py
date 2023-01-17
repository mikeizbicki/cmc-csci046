######################################### 
# first we define the Duck/Dog classes exactly like we did in class

class Duck:
    def __init__(self, weight=None, height=None, name=None):
        self._weight = weight
        self._height = height
        self._name = name

    def __repr__(self):
        return 'Duck(weight=' + str(self._weight) + ',height=' + str(self._height) + ',name=' + self._name + ')'

    def quack(self):
        print('quack... my name is ' + self._name + '... quack')


class Dog:
    def __init__(self):
        self.height = 1
        self.weight = 50
        self._name = 'Lassie'

    def bark(self):
        print('bark... my name is ' + self.name + '... bark!')

########################################
# next we define some Ducks
print('========================================')

donald = Duck(name='Donald')
daisy = Duck(name='Daisy')

ducks = [donald, daisy]

for duck in ducks:
    duck.quack()

########################################
# next we define some Dogs
print('========================================')

lassie = Dog()
lassie.name = 'Lassie'

# In lecture on Monday, I had the following line, which was incorrect
# ```
# lassie.quack = Duck.quack
# ```
# It should be replaced with the following line to make it work:
lassie.quack = lambda: Duck.quack(lassie)

# In this line, the `lambda:` creates an anonymous function that takes no parameters,
# and we manually pass in the lassie parameter as the `self` argument to `Duck.quack`

for duck in ducks + [lassie]:
    duck.quack()
