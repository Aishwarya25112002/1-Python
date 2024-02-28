# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:50:50 2023

@author: hp
"""

''' Write a Numpy program to test element wise for complex nummber, real number in 
and also test if a given number is of scalar type or not '''

import numpy as np
a = np.array([1+1j, 1+0j, 4.5,3,2,2,2j])
print("original array")
print(a)
print("Checking for complex number ")
print(np.iscomplex(a))
print(np.isscalar(3.1)) 
print(np.isscalar([3.1]))

# create a 2D Numpy Array
# Import the libraries

import numpy as np
import matplotlib.pyplot as plt
#consider the list and convert into array

data = [11,22,33,44,55,]
a=np.array(data)
a

#show the numpy array dimension
a.ndim

#to show the numpy array shape
a.shape

#show the numpy array size
a.size

#access the element on second row and third column

a[1] #or a[1][2]

a[0:2]

a[0:2]

#################
#basic Operations
#create a numpy arrayh x

x = np.array([[1,0],[1,2]])

y = np.array([[2,1],[1,2]])

z = x + y

y = np.array([[2,1][1,2]])

#multiply x with 2
z = 2*y

#multiply x with 2
z = 2*x

#multiply x and y
z = x*y

#create a matrix B
B = np.array([1,1],[1,1],[-1,1])
B

#calculate sine of z
A =np.sine(z)

#calculate transpose of matrix
c =np.arary([[1,1],[2,2],[3,3]])
c
