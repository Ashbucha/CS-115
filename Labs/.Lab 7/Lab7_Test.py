from lab7 import *

gor = [
gor3(0,0,0) == 0,
gor3(0,0,1) == 1,
gor3(0,1,0) == 1,
gor3(0,1,1) == 1,
gor3(1,0,0) == 1,
gor3(1,0,1) == 1, 
gor3(1,1,0) == 1,
gor3(1,1,1) == 1 ]

fa =  [
FA(0,0,0) == (0,0),
FA(0,0,1) == (0,1),
FA(0,1,0) == (0,1),
FA(0,1,1) == (1,0),
FA(1,0,0) == (0,1),
FA(1,0,1) == (1,0),
FA(1,1,0) == (1,0),
FA(1,1,1) == (1,1)]

four = [
fourBitAdd((0,0,0,0), (0,0,0,0)) == (0, (0,0,0,0)),
fourBitAdd((0,0,0,1), (0,0,0,0)) == (0, (0,0,0,1)),
fourBitAdd((0,0,1,0), (0,0,0,0)) == (0, (0,0,1,0)),
fourBitAdd((0,0,1,1), (0,0,0,0)) == (0, (0,0,1,1)),
fourBitAdd((1,0,1,0), (1,0,1,0)) == (1, (0,1,0,0)),
fourBitAdd((1,1,1,0), (1,1,1,0)) == (1, (1,1,0,0)),
fourBitAdd((1,0,1,1), (0,1,0,1)) == (1, (0,0,0,0)),
fourBitAdd((0,0,1,0), (0,0,0,1)) == (0, (0,0,1,1)),
fourBitAdd((1,1,1,1), (0,1,1,0)) == (1, (0,1,0,1)),
fourBitAdd((1,1,1,1), (1,1,1,1)) == (1, (1,1,1,0))]

print("gor3: ",sum(gor)*3.75)
print("FA: ",sum(fa)*3.75)
print("four: ",sum(four)*3)
print("Total number of points:", sum(gor)*3.75 + sum(fa)*3.75 + sum(four)*3, "/90.0")
