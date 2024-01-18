# Name: Christopher Buchanan
# Pledge: "I pledge my honor that I abided by Stevens Honor System"
# CS115 Lab 2

'''The dot function is based off of the dot product'''
def dot(L, K):
    if L == [] or K == []: 
        return 0.0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

'''The explode function takes in a string, and returns a list of characters that were in the string'''
def explode(S):
    if not S:
        return []
    else:
        return [S[0]] + explode(S[1:])

'''The ind function uses e to find the index of of the list L at which e was'''
def ind(e, L):
    if L == [] or L == '' or L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

'''The removeAll function removes all values equal to e from list L'''
def removeAll(e, L):
    if L == []:
        return []
    elif L[0] != e:
        return [L[0]] + removeAll(e, L[1:])
    return removeAll(e, L[1:])

'''The myFilter function filters out the even values in the list of L'''
def myFilter(x, L):
    if L == []:
        return []
    elif x(L[0]) == True:
        return [L[0]] + myFilter(x, L[1:])
    return myFilter(x, L[1:])

'''The deepReverse function reverses the list L'''
def deepReverse(L):
    if L == []:
        return []
    elif isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    return deepReverse(L[1:]) + [L[0]]
