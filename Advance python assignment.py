# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:30:41 2023

@author: hp
"""
#que 1.write the python program that take two list ana return 
#true if they have at least one  common member 
#write the python program

def have_common_element(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = have_common_element(list1, list2)
print(result)  
############################################

#que 2.use list comprehension to constract a new list add 6 to
# each item write the python program


original_list = [1, 2, 3, 4, 5]
new_list = [item + 6 for item in original_list]
print(new_list)

##############################################
#que 3.write the python program to reverse string


input_string = "Hello, World!"
reversed_string = input_string[::-1]
print(reversed_string)

##########################################
# que  4.write the python program to iterate over dictionaries using loop

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key in my_dict:
    print(key, my_dict[key])
#######################################################

#que 5.using dict comprehension and conditional  
#argument create a dictionary from the current dictionary 
#where only thekey:value pair with value above 2000 are taken 
#to taken to new dictionary


original_dict = {'item1': 1500, 'item2': 2500, 'item3': 1800, 'item4': 3000}
new_dict = {key: value for key, value in original_dict.items() if value > 2000}
print(new_dict)

###########################################
#que 6. open the file data.txt using file operation write the python program

# Open the file in read mode ('r')
try:
    with open("data.txt", "r") as file:
        # Read and print the contents of the file
        file_contents = file.read()
        print(file_contents)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", str(e))

######################################################
#que 7. write the python program to construct an infinite 
#iterator that return evenly space valued starting with a 
#specified number and step 
def infinite_evenly_spaced_iterator(start, step):
    current = start
    while True:
        yield current
        current += step

start_number = 5
step_size = 2

iterator = infinite_evenly_spaced_iterator(start_number, step_size)

for _ in range(10):
    print(next(iterator))

########################################################
#8. write a python program to filter a list of integers using lambda

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_condition = lambda x: x % 2 == 0
filtered_numbers = list(filter(filter_condition, numbers))
print(filtered_numbers)

#########################################################


#que 8 write a python program to filter a list of integers
# using lambda original list of integer:[1,2,3,4,5,6,7,8,9,10]  
#Even number from the said list:[2,4,6,8,10 ]
# oddnumber from the said list:[1,3,5,7,9] write the python program


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Original list of integers:", numbers)
print("Even numbers from the list:", even_numbers)
print("Odd numbers from the list:", odd_numbers)





