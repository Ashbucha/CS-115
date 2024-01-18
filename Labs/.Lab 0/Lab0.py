'''
Name - Christopher Buchanan
Pedge - I pledge my honor that I have abided by the Stevens Honor System.
CS 115 Lab 0
'''

def same(word):
    '''This function checks if a given ascii string has the same first and last letters. 
    If the string does, the function returns True, if not, the function returns Flase'''
    lower_word = (word.lower())
    if lower_word[0] == lower_word[-1]:
        return True
    else:
        return False



def consecutiveSum(x, y):
    '''This function finds the sum of consecutive integers between two numbers and returns the value'''
    top = (x+y)/2
    bottom = (y-x-1)
    return (top*bottom)
