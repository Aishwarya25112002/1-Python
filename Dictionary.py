# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 09:19:53 2023

@author: hp
"""
#######################
#return value
def get_formatted_name(first_name,last_name):
    full_name=f"{first_name}{last_name}"
    return full_name
musician=get_formatted_name('Aishwarya','Sonawane')
print(musician)

#retuning a dictionary
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('Aishwarya','Sonawane')
print(musician)
#passing list
#useful to pass list function
#name,number,more complex
def greet_users(names):
    for name in names:
        msg=f"Hello,{name.title()}!"
        print(msg)
usernames=['mukta','aishwarya','ankita','pallavi']
greet_users(usernames)
################passing a list
#names,number,more complex object
#such as dictionary
def greet_users(names):
    for name in names:
        msg=f"Hello,{name.title()}!"
        print(msg)
username=['mukta','ankita','pallavi']
greet_users(username)
######################
#passing an arbitary number of argument
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')
#now we can replace the print() call with a loop that run through 
#the list of toppings and describe the pizza being ordered
def make_pizza(*toppings):
    print("\nmaking a pizza with following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')

############################
def make_pizza(size,*toppings):
    print(f"\nmaking a {size}-inch pizza with following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')
##################################################
import pizza
pizza.make_pizza(16,'pepperani')
pizza.make_pizza(12,'mushroom','green peppers','extra cheese')

#importing specific function
from pizza import make_pizza
pizza.make_pizza(16,'pepperani')
pizza.make_pizza(12,'mushroom','green peppers','extra cheese')

#using as to give a function an Alias
from pizza import make_pizza as mp
mp(16,'pepperani')
mp(12,'mushroom','green peppers','extra cheese')
##################################
#using as give module as alias
import pizza as p
p.make_pizza(16,'pepperani')
p.make_pizza(12,'mushroom','green peppers','extra cheese')
#########################
#import all the function in a module
from pizza import *
make_pizza(16,'pepperani')
make_pizza(12,'mushroom','green peppers','extra cheese')
##############################################
#scope of variable
x=x+1
x=6
print(x)
#you cannot reference variable
#until it as assign the variable
######################################################
#initiaze the variable
x=6
x=x+1
print(x)
######################################################
#Ananymous function/Lamda function
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))
add=lambda a,b,c:a+b+c
add(4,5,6)
#########################
def multi(a,b,c):
    multi=a*b*c
    return multi
print(multi(4,5,6))
multi=lambda a,b,c:a*b*c
multi(4,5,6)
##################
val=lambda*args:sum(args)
val(1,2,4,5,6)
val(3,7,8,9,6,4)
#################
def person(name,**data):
    print(name)
    print(data)
    
person(name='Aishwarya',age=16,place='mumbai',mob_no=786548709)

##################
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name='Aishwarya',age=16,place='mumbai',mob_no=786548709)
#####################################
val=lambda**data:sum(data.values())
val(a=2,b=6,c=6,d=7)

##################
max=lambda a,b: x if(a > b) else b
print(max(1,2))
      #####################
      

    
    
    
    
    


    
    
