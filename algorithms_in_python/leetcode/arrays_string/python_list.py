
def random_list(list_size=10):
    return [random.randint(0,list_size) for _ in range(list_size)]

arr = []
print(arr)

arr = [None] * 10
print(arr)
arr = [i for i in range(0,10)]
print(arr)
import random

list_size = 10
arr = random_list(list_size)
print("I am mutable")
print(arr)

print(id(arr))
for i in range(0,list_size):
    arr[i] = 5

print(arr)
print(id(arr))


arr = random_list()
# meethods

print("sorted crates a new array")
a = sorted(arr)
print(a)
print(arr)

print("sort() orders the list in place")
arr = random_list()
print(arr)
print(id(arr))
arr.sort()
print(arr)
print(id(arr))

print(f"reversed {arr.sort(reverse=True)}")


print(f"min {min(arr)}")
print(f"max {max(arr)}")
import statistics as stats

stats.mean(arr)
stats.median(arr)
stats.mode(arr)
stats.stdev(arr)

import numpy as np

print(np.mean(arr))      # Output: 4.75 (mean)
print(np.median(arr))    # Output: 4.5 (median)
print(np.std(arr))       # Output: 3.201562118716424 (standard deviation)
print(np.percentile(arr, 75))  # Output: 7.5 (75th percentile)



# Random List Operations

arr1 = [1] * 4
arr2 = [2] * 4
print(id(arr1))
for i in range(4):
    arr1.append(arr2[i])
print(arr1)
print(id(arr1))

# strings iterate!  `1  ``1 q1`1
s = "abcdefghijklmnop"
arr = [ i for i in s]
print(arr)

