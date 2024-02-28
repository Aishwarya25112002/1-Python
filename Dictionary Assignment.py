# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:42:44 2023

@author: hp
"""

#write the python code script to add a key to dictionary
#sample dictionary:{0:10,1:20}
#Expected result:{0:10,1:20,2:30}

d={0:10,1:20}
print(d)
d.update({2:30})
print(d)
######################(2 Method)
d={0:10,1:20}
print(d)
d[2]=30
print(d)
#########################################
#write a python script to concatenate the following dictionaries
#to create new one
#sample dictionaries
#dict1={1:10,2:20}
#dic2={3:30,4:40}
#dict3={5:50,6:60}

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in(dic1,dic2,dic3):dic4.update(d)
print(dic4)
####################################################################
#write a python script to check whether a given key already
#exist in a dictionary
d={1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in the dictionary')
is_key_present(5)
is_key_present(7)
###################################################################
#Write a python program to iterate over dictionaries using the for loop
d={'x':10,'y':20,'z':30}
for dict_key,dict_value in d.items():
    print(dict_key,':',dict_value)
    

##############################################
#