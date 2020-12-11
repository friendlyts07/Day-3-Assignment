# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:21:31 2020

@author: Tirth
"""


#assignment 4
maxopt=int(input("Enter the max number:"))
def primeno(mynum):
    n=0
    i=2
    
    while i<= mynum//2:
        if mynum % i==0:
            n= n+1
            break
        i=i+1
    if n==0:
        print(mynum, end=" ")
for i in range(2, maxopt):
    primeno(i)
 
    
    
        
    
            
        
        

    

       

             

       

    

    