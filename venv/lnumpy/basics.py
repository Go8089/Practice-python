import array
import numpy as np
def fun():
 arr = array.array('i',[6,8,9])
 # ':' define block, slicing default print(arr[1:3]) arr[:] returns the entire list

 for i in range(0, len(arr)):
     print(arr[i], end=" ")

 arr.append(5)
 arr.append(5)
 arr.insert(1,10)
 arr.pop(0)
 arr.remove(5)
 arr.reverse()
 print(arr[:])

def prime(n):
     i = 2
     while(i < int(n/2)):
      if(n % i == 0):
       return "not"
     return "yes" 
result = prime(13)
print(result)

#Default arg
#keyword arg
#arbitary arg
 #*args, **kargs

def collapse():
  two2d = np.array([[8,5,4],[6,3,4]])
  three3d = np.empty(2,3,3)
  for i in range(0, (len(three3d) - 1)):
    three3d[i] = i + 1
  
