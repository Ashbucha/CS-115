# Name: Christopher Buchanan
# Pledge: "I pledge my honor that I abided by Stevens Honor System"
# CS115 Lab 1

'''Math is already imported, so importing factorial and therefore importing reduce to use both 
factorial and reduce in my code'''
from math import factorial
from functools import reduce

'''the function sum takes the input of x and y and returns the value'''
def sum(x, y):
    return (x+y)

'''the function inverse takes the input of x and moves the value to the denominator'''
def inverse(x):
    y = 1/x
    return y

'''the function e represents the value of e in math'''
def e(n):
    pt_1 = range(1, n+1)
    pt_2 = map(factorial, pt_1)
    pt_3 = map(inverse, pt_2)
    pt_4 = 1 + reduce(sum, pt_3)
    return pt_4
