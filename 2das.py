import numpy as np 

#method 1 , arange use
m1=np.arange(0,9).reshape(3,3)
print(m1 , m1.shape)

# method 2 , list 
'''a=[1,2,3,4,5,6]
b=[4,5,6,6,6,6]
c=[4,5,5,5,5,5]
m2=np.array(a,b,c)
print(m2,m2.shape)'''

# method 3 , feeding list itself
m3=np.array([[1,2,3],[1,2,4],[12,34,55],[22,33,44]])
print(m3,m3.shape)