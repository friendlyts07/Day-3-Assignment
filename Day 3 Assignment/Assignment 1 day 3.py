# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:03:32 2020

@author: Tirth
"""


#assignment 1 
Yourgrade= int(input("Please enter your report card grade: "))
if Yourgrade >= 95:
    print("Your Grade is A+")
elif Yourgrade >= 85 and Yourgrade < 95:
    print("Your Grade is A")
elif Yourgrade >= 75 and Yourgrade < 85:
    print("Your Grade is B+")
elif Yourgrade >= 65 and Yourgrade <75:
    print("Your Grade is B")
elif Yourgrade >= 55 and Yourgrade < 65:
    print("Your Grade is C+")
elif Yourgrade >= 45 and Yourgrade < 55:
    print("Your Grade is C")
elif Yourgrade >= 35 and Yourgrade < 45:
    print("Your Grade is D")
else:
    print("You are Fail")