import numpy as np
#np.newaxis keyword
#converting a 1D array into a row or column vector

arr = np.array([1,2,3,6])
print(arr[:])
ind = 0
ind1 = [0, 1]
print(arr[1:3])
print(arr[arr>3 ])
print(arr[ind1])
print(arr[ind])
print(arr[1])
print(arr[:, np.newaxis])

cube = np.random(3,3,3)
print(cube[...,1])

#Access Multidimensional Numpy array
marr = np.array([[10, 20, 30], [40, 5, 66], [70, 88, 94]])
print(arr[[0,2]])

#shape change
# numpy.reshape() , numpy.resize(())