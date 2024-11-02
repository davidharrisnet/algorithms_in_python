from array import array

# https://docs.python.org/3/library/array.html

ints = [i for i in range(0, 20)]
int_array = array("i", ints)

int_array.insert(1, 60) # insert 60 at index 1

i = int_array[3] # get the data at index 3
int_array.remove(i)

int_array.remove(15)
int_array.remove(16)
int_array.remove(17)

print(int_array.typecode)
print(int_array.itemsize)
print(int_array.buffer_info())

print(int_array)
int_array.byteswap()
print(int_array)

l = int_array.tolist()
print(l)