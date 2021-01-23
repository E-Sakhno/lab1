#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = int(input("Input the first value: "))
y = int(input("Input the second value: "))
addit = x+y
subst = x-y
multi = x*y
try:
    divis = x/y
except:
    divis = 'cannot be divided by zero'
print("Result")
print("addition:\t", addit)
print("substaction:\t", subst)
print("multiplication:\t", multi)
print("division:\t", divis)
