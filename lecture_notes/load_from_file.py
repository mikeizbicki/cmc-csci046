filename='scope.py'
with open(filename) as f:
    # read creates a string
    # readlines creates a list of strings
    xs = f.readlines()
print('xs=',xs)
