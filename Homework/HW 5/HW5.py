# Christopher Buchanan
# Pledge: "I pledge my honor that I abided by Stevens Honor System"
# CS115 Homework 5

memo = {}

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 2
        return 2
    elif n == 1:
        memo[n] = 1
        return 1
    else:
        first_term = fast_lucas(n - 1)
        memo[n - 1] = first_term
        second_term = fast_lucas(n - 2)
        memo[n - 2] = second_term
        return first_term + second_term

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    memo = {}
    def useItOrLoseIt(amount, coin_index):
        '''Decides whether the coins at said index is to be used or not'''
        if (amount, coin_index) in memo:
            return memo[(amount, coin_index)]
        
        if amount == 0:
            memo[(amount, coin_index)] = (0, [])
            return 0, []
        if amount < 0 or coin_index < 0:
            memo[(amount, coin_index)] = (float('inf'), [])
            return float('inf'), []
        
        lostIt = useItOrLoseIt(amount, coin_index - 1)
        useIt = useItOrLoseIt(amount - coins[coin_index], coin_index)
        useIt = (useIt[0] + 1, useIt[1] + [coins[coin_index]])
        
        memo[(amount, coin_index)] = min(lostIt, useIt, key=lambda x: x[0])
        return memo[(amount, coin_index)]
    
    result = useItOrLoseIt(amount, len(coins) - 1)
    return [result[0], result[1]]

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123
print( )
print(fast_change(131, [1, 5, 10, 20, 50, 100])) # [4, [1, 10, 20, 100]]
print(fast_change(292, [1, 5, 10, 20, 50, 100])) # [7,[1, 1, 20, 20, 50, 100, 100]]
print(fast_change(673, [1, 5, 10, 20, 50, 100])) # [11, [1, 1, 1, 20, 50, 100, 100, 100, 100, 100, 100]]
print(fast_change(724, [1, 5, 10, 20, 50, 100])) # [12, [1, 1, 1, 1, 20, 100, 100, 100, 100, 100, 100, 100]]
print(fast_change(888, [1, 5, 10, 20, 50, 100])) # [15, [1, 1, 1, 5, 10, 20, 50, 100, 100, 100, 100, 100, 100, 100, 100]]
