#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
#equations
n = int(input("Enter the number of equations : "))
#input target fucntion
z = [float(x) for x in input("coefficients of objective function: ").split()] 
z = np.array(z)
A = []
#matrix elements entering
print("Enter the coefficient matrix with space: ")

for i in range(0,n):
    row = [float(x) for x in input().split()]
    #add the row to A
    A.append(row)
A = np.array(A)
#add resource vector (dimension is not determined yet!)
b =  [float(x) for x in input("Enter the resources: ").split()]
b = np.array(b)
#column==>axis=1
b = b.reshape([n, 1])
#converte matrix into all positive matrix without any minus element
if(A.min()<0):
    A = A - A.min() + 1
print("The matrix with positive values is: ")
print(A)
#identity matrix , diagonal=1 , other elements=0
S = np.identity(n)
#merge 3 matrixes and creat 'matrix'
matrix = np.concatenate((A, S, b), axis=1)
m = A.shape[1]
#because the coefficients of z are not equal so we should find variables
# we work on column so column == count of variables

z = z.reshape([m, 1])

#we need -Z in the table
# count of zero== n+1
#count of b==1
Z = np.append(-z, np.zeros((1, n+1)))
Z = Z.reshape([1, n + m +1])
#consider rows as horizontal display
matrix = np.concatenate((matrix, Z), axis=0)
#converting to datafram for better displaying
matrix = pd.DataFrame(matrix)
#lable inserting in the table 
#add two strings
for i in range(0,n):
    matrix = matrix.rename(columns={i+m: 'S'+str(i+1)}, index={i: 'S'+str(i+1)})
    #X's lable
for i in range(0,m):
    matrix = matrix.rename(columns={i: 'X'+str(i+1)})
    #the last line lable:Z
matrix = matrix.rename(index={n: 'Z'})
#the last column
matrix = matrix.rename(columns={m+n: 'b'})
display(matrix)

#finding the pivot column by finding the location of minimum Z (column of minimum amount of Z)
pivotCol = matrix.loc['Z'].idxmin(axis=0, skipna=True)
finish = False
#divide a distinct column("bb") into column b in a loop 
while(matrix[pivotCol].loc['Z'] < 0 and not(finish)):
    #store only positive amounts and through out the minus and zero elements
    bb = matrix['b']/matrix[pivotCol]
    bb = bb[bb > 0] 
    #if bb is empty so the algorithm is finished
    if(bb.empty):
        finish = True
        #else.. determine the pivot row 
    else:
        pivotRow = bb.idxmin(axis=1, skipna=True)
        #Now we have PIVOT :)
        pivot = matrix[pivotCol].loc[pivotRow]
        #function for coloring a cell in table (green)
        def style_specific_cell(x):
            color = 'background-color: lightgreen'
            df1 = pd.DataFrame('', index=x.index, columns=x.columns)
            df1[pivotCol].loc[pivotRow] = color
            return df1
        display(matrix.style.apply(style_specific_cell, axis=None))
         #pivot must be 1 so pivot/pivot
        matrix.loc[pivotRow] = matrix.loc[pivotRow] / pivot
        #pivot column except pivot becomes zero by multipling and adding rows etc.

        rowNames = matrix.index.values[matrix.index.values != pivotRow]
        for index in rowNames:
            coef = -matrix[pivotCol].loc[index]
            matrix.loc[index] = matrix.loc[pivotRow] * coef + matrix.loc[index]
        matrix = matrix.rename(index={pivotRow: pivotCol})
        pivotCol = matrix.loc['Z'].idxmin(axis=0, skipna=True)
        display(matrix)

#updating the table
#X lable updating 
print("The answer is: ")
X = ['X'+ str(i+1) for i in range(0,m)]
nash={}
#if we have X in the raw so .. this is our nash and we calcute it

for x in X:
    if x in matrix.index.values:
         nash[x] = round(matrix['b'].loc[x]/matrix['b'].loc['Z'], 4)
    else:
        nash[x] = 0
print(nash)


# In[7]:





# In[ ]:




