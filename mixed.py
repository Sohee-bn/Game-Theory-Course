#!/usr/bin/env python
# coding: utf-8

# In[2]:



import numpy as np


print("Enter the entries for PLAYER 1 in a single line (separated by space): ") 
entries = list(map(int, input().split())) 

A = np.array(entries, dtype = float).reshape(2 , 2) 
print("the first player: \n","Player1=",A)


#calculating the probabilities p, 1-p,q and 1-q 
#p,1-p
g=abs(A[1][1]-A[1][0])
h=abs(A[0][0]-A[0][1])
p1=g/(g+h)
p2=h/(g+h)
print("p=" ,p1,"1-p=" ,p2)
#q,1-q
f=abs(A[1][1]-A[0][1])
m=abs(A[1][0]-A[0][0])
q1=f/(f+m)
q2=m/(f+m)
print("q=" ,q1,"1-q=" ,q2)
#Expected utility
v1=((A[0][0]*g)+(A[1][0]*h))/(g+h)
print("v=",v1)

#creating matrix for player 1 by entering elements 
#zero-sum game so reverse A is B.
B=np.flip(A)
print("the second player: \n","Player2=", B) 

#calculate the probabilities
#p,1-p
i=abs(B[1][1]-B[1][0])
o=abs(B[0][1]-B[0][0])
p11=i/(i+o)
p22=o/(i+o)
print("p=" ,p11,"1-p=" ,p22)
#q,1-q
r=abs(B[1][1]-B[0][1])
s=abs(B[1][0]-B[0][0])
q11=r/(r+s)
q22=s/(r+s)
print("q=" ,q11,"1-q=" ,q22)
#expected tyility
#payoff the game of a player
v2=((A[0][0]*g)+(A[1][0]*h))/(g+h)
print("v=",v2)

