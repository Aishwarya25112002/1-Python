# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:29:16 2023

@author: hp
"""
#Reading data in various format
import pandas as pd
f1=pd.read_csv('C:/1-python/buzzers.csv')
###########
import os
with open('buzzer.csv')as raw_data:
    print(raw_data.read())
#######
    #Reading csv data as lists
import csv
with open('c:/1-python/buzzers.csv')as raw_data:
    for line in csv.reader(raw_data):
        print(line)
   
#Reading csv data as dictionaries
import csv
with open('buzzers.csv')as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
        