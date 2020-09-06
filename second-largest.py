# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:35:12 2020

@author: USER
"""


#find the runner up score
list1 = [] 
  
# number of elements as input 
n = int(input("Enter number of elements : ")) 
  

for i in range(0, n): 
    element = int(input()) 
  
    list1.append(element) # adding the element 
      
print(list1) 

list1.sort()
print(list1)
result = list1[-2]
print("The runner up score is: ",result)