# #Q2
import numpy as np
data1=[1,3,9,12,18]
print(np.array(data1))
data2=[[1,5,2,0],[3,6,4,7]]
print(np.array(data2))
data3=[['7','6'],['5','4'],['3','2']]
print(np.array(data3))
data4=[[11,52,20,50],[34,61,43,17]]
print(np.array(data4))

# #Q3
# arrData1=np.array(data1)
# print(arrData1+arrData1)
# print(arrData1*10)
# print(np.array(data1,dtype='int64'))
# print(np.array(data2,dtype='int64'))
# print(np.array(data3,dtype='int64'))
# print(np.array(data4,dtype='int64'))

#Q4
print(np.zeros((3,5)))
print(np.ones((2,8)))
print(np.random.randn(6,3))

#Q5
arrData1=np.array(data1)
print(arrData1[2:4]**2)

#Q6
Subjects=[['ML','OS','CCN'],['OS','AI','MP'],['CCN','ML','AI']]
arrSubjects=np.array(Subjects)
print(arrSubjects==('ML' or 'AI') )