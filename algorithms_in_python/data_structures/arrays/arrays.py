from array import array
import random

wqs
# https://docs.python.org/3/library/array.html

"""
append end   O(1)
append front O(N)
remove     O(N)
access  O(1)
insert  O(N)
delete  O(N)
"""

size = 10


def random_int():
    return random.randint(0, 1000)


ints = [random_int() for _ in range(0, size)]
int_array = array("i", ints)

# insert
int_array.insert(1, 60)

i = int_array[3]
int_array.remove(i)
print(int_array.typecode)
print(int_array.itemsize)
print(int_array.buffer_info())

print(int_array)
int_array.byteswap()
print(int_array)

l = int_array.tolist()
print(l)