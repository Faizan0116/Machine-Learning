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
arrSubjects[~((arrSubjects == 'ML') | (arrSubjects == 'AI'))]=0
print(arrSubjects)

#Q7
print(np.array(data2).T)
print(np.array(data3).T)
print(np.array(data4).T)

#Q8
arrData2=np.array(data2)
arrData4=np.array(data4)
print(np.vstack((arrData2,arrData4)))
print(np.hstack((arrData2,arrData4)))

#Q9
arrData2=np.array(data2)
arrData2mean=arrData2.mean(1)
print(arrData2)
print(arrData2mean.reshape((2,1)))
demeaned=arrData2-arrData2mean.reshape(2,1)
print(demeaned)
print(demeaned.mean(1))

#Q10
arrData2=np.array(data2)
print(arrData2.reshape((4,2)))

#Q11
Data5=np.array([[60,70,50],[40,60,80],[70,55,65]])
print(Data5)
print(Data5.max(axis=0).reshape(3,1))


#Q14
x=np.random.randn(4,4)
print(x)
print(x.T)

mat=x.T.dot(x)
print(mat)
matInv=np.linalg.inv(mat)
print(matInv)
print(mat.dot(matInv))