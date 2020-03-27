import numpy as np
arr = np.arange(0,11)
print(arr)

#slicing of bytearray
print(arr[0:5])

#replace of values
arr[0:5] = 100
print(arr)


arr_copy = arr.copy()
print(arr_copy)


#2dimensional array
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)
print(arr_2d[1])

arr2d_new = np.zeros((10,10))
print(arr2d_new)

#shape provides the array dimension lengths
length,width=arr2d_new.shape
print(length,width)


#replacing array values:
for i in range(length):
    arr2d_new[i]=i
print(arr2d_new)


num=0
for i in range(length):
    if i==num:
        arr2d_new[i] = i
    num = num + 1
print(arr2d_new)


#slicing an array into array
print(arr2d_new[[3,4,7]])


"""Array Transposition"""

arr = np.arange(50).reshape((10,5))

