# Christopher Buchanan
# Pledge: "I pledge my honor that I abided by Stevens Honor System"
# CS115 Lab 6

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    #Q1: In a comment in your file, under your isOdd function, include the complete base-2 representation of the number 42.
    #Answer: Since 42 is an even number, when "42%2", the output is 0. 42/2 = 21.0 if the remainder was not 0, it wouldn't be even.
    if n % 2: # n%2 = 1
        return True #odd
    else: # n%2 = 0
        return False #even

#Q2: In 1-2 sentences in a comment in your file, explain your answer to these two questions.
    #A.If you are given an odd base-10 number, what will the least-significant bit - the rightmost bit - be in its base-2 representation? 
    #B.Similarly, if you are given an even base-10 number, what will the least-significant bit - the rightmost bit - be in its base-2 representation?
'''
Binary Table:
__________________________
|256|128|64|32|16|8|4|2|1|
|0  |0  |0 |1 |0 |1|0|1|0| = 42
|0  |0  |0 |1 |0 |1|0|1|1| = 43
__________________________
'''
#Q2A Answer: The least significant bit in its base-2 representation will always be 1 becasue odd numbers will always have use 1 at the end of their binary string (refer to binary table above)
#Q2B Answer: Since he least significant bit in its base-2 representation for odd numbers will always be 1, even numbers will always be 0 because even numbers are divisible by 2.

#Q3: Briefly explain how the value of the original number is changing in another comment in your file.
#Answer: So if the original binary is 1010 which in binary is equal to 10, when removing 0 from the end of 1010, leaving 101 which in binary is equal to 5. And if the original binary is 1011 which in binary is equal to 11, when removing 1 from the end of 1011, leaving 101 whch in binary is equal to 5. Either way, it changes the binary to decimal form by removing those binary digits.

#Q4: 
    #A/B - Since Y = N/2, the binary representation of Y will be the binary representation of N but with the rightmost bit removed because dividing by 2 in base-2 is equivalent to shifting the digits one place to the right.
    #A.If N is odd - need to add a 1 to the righmost position.
    #B.If N is even - need to add a 0 to the righmost position.


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    else:
        return numToBinary(n // 2) + str(n % 2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if not s:
        return 0
    
    return int(s[0]) * (2 ** (len(s) - 1)) + binaryToNum(s[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return ('0' * 8 + numToBinary(binaryToNum(s) + 1))[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0:
        return
    if n > 0: 
        return count(increment(s), n - 1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    else:
        return numToTernary(n // 3) + str(n % 3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if not s:
        return 0
    
    return int(s[0]) * (3 ** (len(s) - 1)) + ternaryToNum(s[1:])

#Q5: In a comment or triple-quoted string, explain what the ternary representation is for the value 59, and why it is so.
#Answer: In ternary (base-3), there are only 3 possible digits: 0, 1, and 2. To find the ternary representation of 59:
#59 / 3 = 19 remainder 2
#19 / 2 = 6 remainder 1
#6 / 3 = 2 remainder 0
#2 / 3 = 0 remainder 2
#Then reading the remainders from top to bottom we get 2102 which is the ternary value of the decimal value 59.
