import numpy as np

#allow perform arithmetic operations without reshaping the array
#reduce memory usuage
#eliminating need for loop

#automatically adjusts the smaller array to match the larger array shape by replicating its values

ary_1 = np.array([1,2,43])

print(ary_1 + 10)

ary_2 = np.array([[12,45,78],[78,90,34]])

ad = ary_1 + ary_2
ad1 = ary_1 - ary_2
ad2 = ary_1 * ary_2

print(ad)
print(ad1)
print(ad2)

#Normalizing Image Data
img = np.array([[56,78,89],
                [67,89,35],
                [78,98,45]])
m = img.mean(axis = 0)
print(m)
s = img.std(axis=0)
print(s)
res = (img - m) / s  #Data standarization
print(res)

#Centering data in machine learning

data = np.array([[10,20],
                [15,25]])

d = np.mean(data, axis = 1)
sd = np.std(data, axis = 1)
print(sd)

