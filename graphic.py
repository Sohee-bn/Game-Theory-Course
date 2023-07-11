#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import pandas for creating the matrix
import pandas as pd
# count of strategies( count of columns) and entering rows by n elements 
n = int(input("Enter the number of strategies : "))
upRow = [float(x) for x in input("Enter the first row of matrix with space: ").split()]
downRow = [float(x) for x in input("Enter the second row of matrix with space: ").split()]

#creating the matrix(type: dictionary)
matrix = {}

matrix['p'] = upRow
matrix['1-p'] = downRow

#change the type of the matrix into dataframe 
print(pd.DataFrame(matrix).transpose())


# In[8]:


#import pandas for creating the matrix
import pandas as pd
# count of strategies( count of columns) and entering rows by n elements 
n = int(input("Enter the number of strategies : "))
upRow = [float(x) for x in input("Enter the first row of matrix with space: ").split()]
downRow = [float(x) for x in input("Enter the second row of matrix with space: ").split()]

#creating the matrix(type: dictionary)
matrix = {}

matrix['p'] = upRow
matrix['1-p'] = downRow

#change the type of the matrix into dataframe 
print(pd.DataFrame(matrix).transpose())
#import needed libraries
import matplotlib.pyplot as plt
import numpy as np

# minimum and maximum amount of Y according to rows (p=0 and p=1)
minY = min(matrix['p'])
if(min(matrix['1-p'])<minY):
    minY = min(matrix['1-p'])
maxY = max(matrix['p'])
if(max(matrix['1-p'])>maxY):
    maxY = max(matrix['1-p'])
    
#draw the line by 500 points in [0,1]boundary    
for i in range(0, n):
    p = np.linspace(0,1,500)
#equation of lines:
    plt.plot(p, (matrix['p'][i] - matrix['1-p'][i]) * p + matrix['1-p'][i]) 

#finding intersections
intersectionsX = {}
intersectionsY = {}
for i in range(0,n):
    
    intersectionsX[i] = {}
    intersectionsY[i] = {}
    
    for j in range(0,n):
        # search in zero till n'th line and find intersections 
        
        if(matrix['p'][i] + matrix['1-p'][j] - matrix['p'][j] - matrix['1-p'][i] != 0): 
            x = (matrix['1-p'][j] - matrix['1-p'][i])/(matrix['p'][i] + matrix['1-p'][j] - matrix['p'][j] - matrix['1-p'][i])
            #for making sure the dominator is not zero
            if(x<0 or x>1):
                 intersectionsX[i][j]  = -1
            else:
                intersectionsX[i][j] = x
                #Y of intersection point
                y = (matrix['p'][i] - matrix['1-p'][i]) * x + matrix['1-p'][i]
                intersectionsY[i][j] = y
                #Bold intersection by scatter
                plt.scatter(x, y, color='black')
                
        else:
            #if no intersection
            intersectionsX[i][j] = -1

#plotting intersections in x[0,1] and Y[min, Max]
plt.xlim(0,1)
#1 is used for better illustration
plt.ylim(minY-1, maxY+1)
#if there is no intersection:
if(all(x == -1 for x in intersectionsX.values())):
    print("There is no answer for the problem")
else:
    y = max(intersectionsY)
    for i in range(0,n):
        for j in range(0,n):
            #if intersection is not -1 (absolutely we have an intersection) amd we have a minimum Y[i][j] so:
            if(intersectionsX[i][j] != -1 and intersectionsY[i][j] <= y):
               #find L1 and L2 as two lines which has intersection
                y = intersectionsY[i][j]
                l1 = min(i,j)
                l2 = max(i,j)
    #find L1 and L2 in the matrix and print it.
    print("The final answer is: ")
    print(pd.DataFrame(matrix).transpose()[[l1, l2]])
    line1 = (matrix['p'][l1] - matrix['1-p'][l1]) * p + matrix['1-p'][l1]
    line2 = (matrix['p'][l2] - matrix['1-p'][l2]) * p + matrix['1-p'][l2]
    plt.fill_between(p, np.minimum(line1, line2), minY-1, color='grey', alpha='0.5')


# In[ ]:




