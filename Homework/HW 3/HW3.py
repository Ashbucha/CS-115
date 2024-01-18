# Christopher Buchanan
# Pledge: "I pledge my honor that I abided by Stevens Honor System"
# CS115 Homework 3

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here
def giveChange(amount, coins):
    def dp(amount, coin_index):
        if amount == 0:
            return 0, []
        if amount < 0 or coin_index < 0:
            return float('inf'), []
        without_this_coin = dp(amount, coin_index - 1)
        with_this_coin = dp(amount - coins[coin_index], coin_index)
        with_this_coin = (with_this_coin[0] + 1, with_this_coin[1] + [coins[coin_index]])
        return min(without_this_coin, with_this_coin, key=lambda x: x[0])
    result = dp(amount, len(coins) - 1)
    if result[0] == float('inf'):
        return None
    return [result[0], result[1]]
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    letter_values = dict(scores)
    
    def score(word):
        return sum(map(lambda letter: letter_values[letter], filter(lambda letter: letter in letter_values, word)))

    annotated_words = list(map(lambda word: [word, score(word)], dct))
    return annotated_words

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n <= 0 or not L: 
        return[]
    return [L[0]] + take(n-1, L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n <= 0:
        return L
    elif n >= len(L):
        return ""
    else:
        return L[n:]
