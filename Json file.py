# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:15:04 2023

@author: hp
"""
#####################################
         ###############  JSON FILE HANDLING #################
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

######################

import json
username=input("What is your name?")
filename='username.json'
with open(filename,'w')as f:
    json.dump(username, f)
print(f"we'll remember  you come back {username}")
#############################
import json
filename='username.json'
with open(filename) as f:
    username= json.load(f)
print(f"Welcome back,{username}!")
##################################

filename='username.json'
try:
    with open(filename)as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("What is your name? ")
    with open(filename,'w')as f:
        json.dump(username,f)
        print(f"we'll remember you when you come back,{username}")
else:
    print(f"welcome back,{username}!")

 
    
