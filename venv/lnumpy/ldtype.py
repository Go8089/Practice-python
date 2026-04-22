import numpy as np

np.dtype('>i4')

arr = [4,5,6,7,9]
print(np.array(arr))

arr = [4,5,6,7,8]
arr1 = [7,89,78,8,9]
arr2 = [90,56,89,34,9]

sa_arr = np.array([arr,
                   arr1,
                   arr2], np.dtype(np.int32))

print(sa_arr.shape)
print(sa_arr.dtype)

print(sa_arr)

#structured arrays using dtype
#where each element behaves like a small record with named fields

dt = np.dtype([('name', np.str_, 16),('scores', np.float64,(2,)), ('id', np.int32, (1))])
data = np.array([('Gopal', (1.1, 5.0), (1)), ('Gopal', (1.0, 5.0), (1)), ('Gopal', (1.0, 5.0), (1))], dtype=dt)

for i in range(0, 3):
    print(data[i])

print(data[1]['name'])
print(data[0])
print(data['name'])
print(data[2]['scores'])
