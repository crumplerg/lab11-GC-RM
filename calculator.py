"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be greater than 0 and not equal 1.")

    if b <= 0:
        raise ValueError("Argument must be greater than 0.")

    return math.log(b, a)

def exp(a, b):
    return a ** b

