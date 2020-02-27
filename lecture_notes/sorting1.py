
def linear_search_iterative(xs,val):
    for i in range(len(xs)):
        if xs[i]==val:
            return i


def linear_search_recursive(xs,val):
    def go(i):
        if xs[i]==val:
            return i
        if i<len(xs)-1:
            return go(i+1)
    return go(0)


def insertion_sort(xs):
    for i in range(1,len(xs)):
        current_value = xs[i]
        position = i
        while position>0 and xs[position-1]>current_value:
            xs[position] = xs[position-1]
            position = position-1
        xs[position] = current_value
