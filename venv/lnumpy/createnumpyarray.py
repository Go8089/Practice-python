import numpy as np
#1
arr = np.array([[45,56],[78,67]], np.dtype('>i4'))
print(arr[:])

#2  fromiter() create a new 1-D array from an iterable object.
# numpy.fromiter(iterable, dtype, count=-1)

var = "gopal"
var1 = [4,6,7,8]
arr1 = np.fromiter(var, dtype='U1')
print(arr1)
arr2 = np.fromiter(var1, dtype='i4')
print(arr2)

#3returns evenly spaced values numpy.arange( start , stop, step , dtype=None )
print(np.arange(1, 20, 4, dtype=np.int32))

#4 numpy.empty(shape, dtype=float, order='C')
arr3 = np.empty([4,3], dtype = np.int32, order = 'C')
for i in range(len(arr3)):
    arr3[i] = i
print(arr3[:])

#5 numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
#6  numpy.zeros(shape, dtype=None, order='C')
#7  numpy.ones(shape, dtype=None, order='C')
#8 af = np.full((2, 2), 7)


#Create Python Numpy Arrays Using Random Number Generation
arr = np.random.randint(5, 15, size=(2, 2, 4))

array = np.random.randn(2, 2 ,2)
print("3D Array filled with random values : \n", array);
     
# Multiplying values with 3
print("\nArray * 3 : \n", array *3)

# Or we cab directly do so by 
array = np.random.randn(2, 2 ,2) * 3 + 2
print("\nArray * 3 + 2 : \n", array)

ar = np.random.rand(2, 3)

#Create Python Numpy Arrays Using Matrix Creation Routines
im = np.eye(3)
da = np.diag([1, 2, 3])
a0 = np.zeros_like(da)
a1 = np.ones_like(da)

print(im)
print(da)
print(a0)
print(a1)