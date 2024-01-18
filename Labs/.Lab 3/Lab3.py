# Christopher Buchanan
# Pledge: "I pledge my honor that I abided by Stevens Honor System"
# CS115 Lab 3

def change(amount, coins):
    '''The function change returns the amount of coins that make up the amount from the coins list. If the amount can not be fully setted, it returns inf to show its not possible'''
    if amount == 0:
        return 0
    elif amount < 0 or coins == []:
        return float('inf')
    elif amount > 0:
        loseIt = change(amount, coins[1:])
        useIt = 1 + change(amount - coins[0], coins)
    return max(useIt, loseIt)
