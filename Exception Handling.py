# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:13:45 2023

@author: hp
"""
################EXCEPTION HANDLING#################
#Error signifinifies a situation that mostly
#happen due to absence of system resource
#the exception are issue can be appear
#exception are handle with try exceppt block
#Handling the zeroDivisionError Exception
#It majorly arise in the code or program
#authored by the developer
print(5/0)

#using try and except block
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    ###########################
a=5
b=7
c=a+b
print(5/0)
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
'''  
################################
a=5
b=7
c=a+b
#print(5/0)

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print(c)
############################################

         #Handling the fileNotFoundError Exception
filename='alice.txt'
with open(filename,encoding='utf-8') as f:
    contents=f.read()
####################################################
    
filename='alice.txt'
try:
    with open(filename,encoding='utf-8')as f:
        contents=f.read()
except FileNotFoundError:
    print(f"sorry,the file{filename} does not exist")
##########################################################
         #Storing the data
'''
many program will ask user to
input certain kinds of informaion
might allow user to store preferences
user provide the data structure 
such as list and dictionaries
when user close a program
you'll almost always want to save
the information to be save
'''
#JSON(Javascript object notation)
#python support json with built packages called as 'JSON'
#JSON FILE like dictionary it  start with {}
#campare in python or json
#dict-object
#int -number
#using json.dump() and json.load()
import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w')as f:
    json.dump(numbers,f)
 
    

