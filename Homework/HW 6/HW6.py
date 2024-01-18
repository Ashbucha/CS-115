# Christopher Buchanan and Mikayla Minton
# Pledge: "I pledge my honor that I abided by Stevens Honor System"
# CS115 Homework 6

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def compress(S): #x-count
    """Compresses a binary string S at its x-values"""
    if not S:
        return ''

    if S[0] == '0':
        x_count = 1 + checkNext(S[1:], '0')

        if x_count > MAX_RUN_LENGTH:
            return '1' * COMPRESSED_BLOCK_SIZE + compress1(S[MAX_RUN_LENGTH:])
        else:
            binary_count = numToBinary(x_count)
            return '0' * (COMPRESSED_BLOCK_SIZE - len(binary_count)) + binary_count + compress1(S[x_count:])
    else:
        return '0' * COMPRESSED_BLOCK_SIZE + compress1(S)

def compress1(S): #y-count
    """Compresses a binary string S at its y-values"""
    if not S:
        return ''

    if S[0] == '1':
        y_count = 1 + checkNext(S[1:], '1')

        if y_count > MAX_RUN_LENGTH:
            return '1' * COMPRESSED_BLOCK_SIZE + compress(S[MAX_RUN_LENGTH:])
        else:
            binary_count = numToBinary(y_count)
            return '0' * (COMPRESSED_BLOCK_SIZE - len(binary_count)) + binary_count + compress(S[y_count:])
    else:
        return '0' * COMPRESSED_BLOCK_SIZE + compress(S)

def checkNext(S, num):
    """Looks for additional 0s or 1s in the list"""
    if not S:
        return 0

    if S[0] == num:
        return 1 + checkNext(S[1:], num)
    else:
        return 0

def numToBinary(n):
    """Converts an integer to a binary string"""
    if n == 0:
        return ''
    else:
        return numToBinary(n // 2) + str(n % 2)
    
'''
Q1 - Explain what is the largest number of bits that your compress algorithm could
possibly use to encode a 64-bit string/image.
Q1 Answer - There is no limit. The compress algorithm in this code should be able to encode any 64-bit string or image.
'''

def uncompress(S):
    """Inverts a compressed string"""
    def uncompress1(n, s):
        """Helper Function: Uses the compress function to iterate through x and y values and generate an uncompressed string"""
        if not s:
            return ''

        block_size = binaryToNum(s[:COMPRESSED_BLOCK_SIZE])

        if n == 1:
            return '1' * block_size + uncompress1(0, s[COMPRESSED_BLOCK_SIZE:])
        elif n == 0:
            return '0' * block_size + uncompress1(1, s[COMPRESSED_BLOCK_SIZE:])
    
    def binaryToNum(S):
        """Converts a binary string to an integer"""
        if not S:
            return 0
        
        return int(S[0]) * (2 ** (len(S) - 1)) + binaryToNum(S[1:])
    return uncompress1(0, S)

def compression(S):
    """Calculates the compression ratio (ratio fo the compressed image to the original size of the given image)"""
    return len(compress(S))/len(S)

'''
Q2 - Describe the tests that you conducted and the compression ratios that you found.
Q2 Answer - I tested a few imagines I thought up, and found that the longer the compressed string is, the greater the compression value becomes.

Q3 - Argue to NASA that Professor Lai is Lai-ing—such an algorithm cannot exist!
Q3 Answer - Since his function always will return a shorter string than the one inputted, he looses data everytime he compresses a string.
'''

sequence = '0' * 64
print(compress(sequence))
print(uncompress("1111100000111110000000010"))
