# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:35:55 2023

@author: hp
"""

#write python program to create an iterator
#from serveral iterables in a sequence and display
#the type and element of the new iterator

from itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#list
result=chain_func([1,2,3],['a','b','c','d'],[4,5,6,7,8,9])
print("Type of the new iterator:")
print(type(result))
print("Element of new iterator:")
for i in result:
    print(i,end='  ')
    
#tuple
result=chain_func((1,2,3),('a','b','c','d'),(4,5,6,7,8,9))
print("Type of the new iterator:")
print(type(result))
print("Element of new iterator:")
for i in result:
    print(i,end=' ')
####################################################
  
#write python program that generate the runing product
#of elements in an iterable
from itertools import accumulate#mathmatical operator
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
#list
result=running_product([1,2,3,4,5,6,7])
print("running product of list:")
for _ in result:
    print(_)

##########################################################
#  Tuple  
result=running_product((1,2,3,4,5,6,7))
print("running product of Tuple:")
for i in result:
     print(i)
     ######################################
#Write a python program to construct an infinite iterator 
#that return evenly spaced values starting with a specified number and step

import itertools as it
start=10
step=1
print("The starting number is ",start,"and step is",step)
my_counter=it.count(start,step)
print("The said function print never-ending items:")
for i in my_counter:
    print(i)
###################################################
#write python program to generate an infinite cycle
#of element from an iterable
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
#following loop will run for ever
#list
result=cycle_data(['A','B','C','D'])
print("The said function print never-ending items")
for i in result:
    print(i)
##############################################
#string
result=cycle_data('python itertools')
print("The said function print never-ending items")
for i in result:
    print(i)
###########################################
#write a python program to make an itertool that drop
#element from the iterable as soon as an element is positive number
import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x : x < 0,nums)
nums=[-1,-2,-3,4,-10,2,0,5,12]
print("original list: ",nums)
result=drop_while(nums)
print("Drops elements from the iterable when a positive number arises\n",list(result))
###############################################

