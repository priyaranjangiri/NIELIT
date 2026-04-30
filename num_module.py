import numpy as np

#1d array
x=np.array([1,2,3])

#2d array
y=np.array([[1,2],[3,4]])

#3d array
z=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(x)
print(y)
print(z)

print(z.shape)
print(z.ndim)
print(z.size)
print(z.dtype)
print(z.itemsize)