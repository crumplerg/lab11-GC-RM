"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot find the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b) # no error checking needed, negative numbers are allowed.

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Divide by zero")
    else:
        return b / a

def log(a, b):
    if b <= 0 or a <= 0:
        raise ValueError("Cannot use a negative number")
    
    if a == 1:
        raise ValueError("Argument cannot be exactly 1.")
    
    return math.log(a, b)

def exp(a, b):
    return a**b
