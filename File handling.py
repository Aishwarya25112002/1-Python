# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:17:28 2023

@author: hp
"""
#File Handling
with open('pi_digits.txt') as file_object:
    #The open() function needs
    #one argument: the name of the file you want to open.
    contents = file_object.read()
print(contents)
#####################
with open('pi_digits.txt') as file_object:
    #The open() function needs
    #one argument: the name of the file you want to open.
    contents = file_object.read()
print(contents.rstrip())
#rstrip method remove the whilespace
#character from side of string
##########################################
file_path='c:/1-python/pi_digits.txt'
with open(file_path)as file_object:
    contents=file_object.read()
print(contents.rstrip())

####################################
#Reading line by line
filename='pi_digits.txt'
#we assign the name file we're reading from to a variable
with open(filename)as file_object:
#we again use the with syntax
#let file open and close
#the file properly
    for line in file_object:
        print(line)
        
##########################################
#These blank line appear bcz an invisible newline
#character is at the end of each line in the text file
#using rstrip()on each line in
#the print()call eliminate these extra line
filename='pi_digits.txt'
with open(filename)as file_object:
    for line in file_object:
        print(line.rstrip())
        
########################################
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))
###########################################
#one of the simplest ways to save data is write it
#to a file .when you write text file
filename='programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming in python")
    
###################################################
#writing multiple line
filename='programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming in python.")
    file_object.write("I love creating new games.")
#################################
filename='programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming in python.\n")
    file_object.write("I love creating new games.\n")
########################################
#Appending a file
#you can open file in append mode
#python doesn't erase the content of the file
#before returing the file object.
filename='programming.txt'

with open(filename,'a') as file_object:
    #we use the 'a' argument to open the file for appending
    #rather than writing over the existing file
    file_object.write("I also love finding meaning in a large dataset.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    


    
    
