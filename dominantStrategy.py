#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
n = int(input("Enter the number of rows : "))
m = int(input("Enter the number of columns: "))
A = []
for i in range(0,n):
    row = [float(x) for x in input().split()]
    A.append(row)
A = np.array(A)
#change for status ; size of columns and type: boolean
change = np.full(m, False)

#starts comparing from the first column and compare it with next columns
for i in range(0,m):
    for j in range(i+1,m):
        #If all of elements are smaller than the other ==> change=TRUE
        if all(x == True for x in A[:,i]<A[:,j]):
            change[i] = True
            
#True columns must be deleted
A = np.delete(A, np.where(change==True), axis = 1)
m = A.shape[1]
#updating columns and change
change = np.full(m, False)
for i in reversed(range(0, m)):
    for j in reversed(range(0, i)):
        if all(x == True for x in A[:,i]<A[:,j]):
            change[i] = True
A = np.delete(A, np.where(change==True), axis = 1)
print(A)
print("The final answer is: ")

#if only one column remains then return max ==>(the max of rows that is dominant)
if A.shape[1]==1:
    print(np.amax(A))
    
#if only one column remains then transpose matrix (to change it into 2*n form to use it in our graphical model)
elif A.shape[1]==2:
    print(A.T)
#if matrix doesnt have dominant column then print it itself
else:
    print(A)


# In[ ]:




