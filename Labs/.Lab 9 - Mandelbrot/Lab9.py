# mandelbrot.py
# Lab 9
# Name: Christopher Buchanan
# Pledge: I pledge my honor that I have abided by the Stevens Honor System

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:
def mult(c,n):
    '''mult uses only a loop and addition to multiply c by the integer n.'''
    result = 0
    for x in range(n):
        result += c
    return result

def update(c,n):
    '''update starts with z=0 and runs z = z**2 + c for a total of n times. It returns the final z.'''
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

def inMSet(c,n):
    '''takes as input a complex number c and an integer n, returns a Boolean: True if the complex number c is in the Mandelbrot set and False otherwise.'''
    z = 0
    for x in range(n):
        z = z**2 + c
        if not abs(z) <= 2:
            return False
    return True

def weWantThisPixel(col, row):
    """ a function that returns True if we want the pixel at col, row and False otherwise"""
    if col%10 == 0 and row%10 == 0:
        return True
    else:
        return False

def test():
    """ a function to demonstrate how to create and save a png image"""
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    image.saveFile()

#Changing the "and" to an "or" does not change the test.png

def scale(pix,pixMax,floatMin,floatMax):
    '''scale takes in pix, the CURRENT pixel column (or row) pixMax, the total # of pixel columns
    floatMin, the min floating-point value floatMax, the max floating-point value
    scale returns the floating-point value that corresponds to pi'''
    return floatMin + ((pix / pixMax) * (floatMax - floatMin))

def mset():
    '''creates a 300x200 image of the Mandelbrot set'''
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        x = scale(col, 300, -2, 1)
        for row in range(height):
            y = scale(row, 200, -1, 1)
            c = x + y*1j
            if inMSet(c, 25):
                image.plotPoint(col, row)
    image.saveFile()

print(mult(6,7))
print(update(1,3))
c = 3+4j
print(inMSet(c,25))
