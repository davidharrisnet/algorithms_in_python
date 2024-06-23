import numpy as np

# Array Multiplication
a = np.array([[1,2,-1], [0,-5,3]])
b = np.array([[4]])
print()
print("Array multiply")
print(a*b)
print(np.multiply(a,b))
print()
print("Dot Product")
# Matrix dot product 

a = np.matrix([[1,2,-1], [0,-5,3]])

b = np.matrix([4,3,7])
print(a)
print(b)
print(np.dot(a,b.T))
print(a * b.T)
print()
print("Identity")
print(np.identity(4))
print()