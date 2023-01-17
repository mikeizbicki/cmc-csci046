

# returns just a single factorial number
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# write a function that returns all factorials from 1 up to n
# computational complexity: O(n^2)
def naive1(n):
    ret = []
    for i in range(n):
        ret.append(factorial(i))
    return ret

# runtime complexity is O(n)
# still has a downside: have to allocate this list, and keep it allocated
# naive2(100000000000)
# space complexity is O(n)
def naive2(n):
    result = 1
    ret = []
    for i in range(1,n+1):
        result *= i
        ret.append(result)
    return ret

#for i in naive2(10000000000):
#    print(i)


# yield function lets us write functions with O(1) space complexity instead of O(n)
def not_naive(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result

# functions using yeild are generators very common in python
for i in not_naive(10000000000):
    print("i=",i)
