# list creation

# empty string
i = []


# initializing with None
j = [None] * 10
print(j)

# initializing with 0
j = [0] * 10
print(j)
# letters
j = ["a"] * 10
print(j)

j = ["a","b"] * 4
print(j)


def initlist(*args, n=10):
    return [i for i in args] * n

j = initlist(1,2,3,n=4)
print(j)

# strings are immutable
lstring = "aaaaaaaaaa"
# but we can convert a string to an list
m = [ i for i in lstring] # you can iterate through a string
# replace by index
m[4] = 'z'
m[5] = 'z'
# and recreate the string
n = ''.join(m) # you can recreate a string from a list
print(n)

# list operations
# reverse list
x = list(range(10,0,-1))
print(x)
# even numberes
x = list(range(0,10,2))
print(x)

# apppend to the end in place
x.append(-2)
print(x)

# pop from the end
x.pop()
print(x)

# add to the front
x = list(range(1,11)) # range is not inclusive
x.reverse()  # reverse in place
x.append(-1)
x.reverse() # reverse in place
print(x)

# by hand
print("manually")
x = list(range(1,11))
print(x)
# https://github.com/python/cpython
# https://github.com/python/cpython/blob/815061cbab0ff7e3b0062191bae846a83c23c79a/Objects/listobject.c#L34
def reverse(arr):
    i = 0
    j = len(arr) -1

    while(i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j -=1
reverse(x)        
print(x)
x.append(-1)
reverse(x)
print(x)

# another way to revese. # This is what python source does
# https://github.com/lucasayres/python-tools/blob/master/tools/reverse.py
print(x[::-1])

a = "a"
b = "b"
print(b > a)
# ord is the ascii value of a character
print(ord(a) < ord(b))


# string operations

a = "abcdefg"
print(a[3])