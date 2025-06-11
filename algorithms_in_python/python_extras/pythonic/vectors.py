import numpy as np

A = np.random.randn(4,5)

B = np.sum(A, axis=1)

print(B.shape)