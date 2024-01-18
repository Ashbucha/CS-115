# Name: Christopher Buchanan
# Pledge: "I pledge my honor that I abided by Stevens Honor System"
# CS115 Homework 1

'''Math is already imported, so importing factorial and therefore importing reduce to use both 
factorial and reduce in my code'''
#from math import factorial
from functools import reduce

'''the function sum takes the input of x and y and returns the value'''
def sum(x, y):
    return x + y

def mult(x, y):
    return x * y

'''the function factorial takes the input of n, and returns the factorial of n'''
'''the if/else statement is if the input is negative, it will follow else, and return "fail"'''
def factorial(n):
    if (n >= 0):
        all_values = range(1, 1+n)
        mapped = map(int, all_values)
        reduced = reduce(mult, mapped)
        return(reduced)
    else:
        return "fail"

'''the function mean takes the input of L which is a list, adds the values in the list, and 
divides the sum of numbers by how many are in the list, to give the mean value'''
'''the if/elif statement is for the "commented test", which if ran, returns 0. In other words, 
if there are no values in the list, the elif returns 0.'''
def mean(L):
    if (len(L) > 0):
        map(factorial, list(L))
        a = reduce(sum, L)
        return a/(len(L))
    elif (len(L) <= 0):
        return 0
