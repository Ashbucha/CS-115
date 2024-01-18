# Christopher Buchanan
# Pledge: "I pledge my honor that I abided by Stevens Honor System"
# CS115 Lab 4

def knapsack(capactity, itemList):
    '''The knapsack function takes an int: capacity representing the maximum weight the knapsack can hold, 
    and a list of lists: items where each sublist contains the weight and value of an item. 
    The function returns a list with two elements: the maximum capacity and the selected items.'''
    if itemList == [] or capactity == 0:
        return [0, []]
    if itemList[0][0] > capactity:
        return knapsack(capactity, itemList[1:])
    elif capactity > 0 or itemList != []:
        loseIt = knapsack(capactity, itemList[1:])
        useIt = knapsack(capactity - itemList[0][0], itemList[1:])
    return max(loseIt, [useIt[0] + itemList[0][1], [itemList[0]] + useIt[1]])
