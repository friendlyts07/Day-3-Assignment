# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:30:42 2020

@author: Tirth
"""


#assignment 2

for n in range(1, 1000):
    if n>1:
        for z in range(2, n) :
            if (n%z) ==0:
                break
        else:
          print(n)
            
   
        
        