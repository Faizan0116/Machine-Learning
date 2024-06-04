import numpy as np
data1 = [6, 7.5, 8, 0, 1]
arr1=np.array(data1)
print(arr1.ndim)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2=np.arange(12)
arr2=arr2.reshape(4,3)

print(arr2)
print(arr2.mean(1))
demeaned=arr2-arr2.mean(0)
print(demeaned)
print(demeaned.mean(0))
# print(arr2.shape)