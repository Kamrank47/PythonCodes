# import funtions array module
from array import *

# initialize array
arr = array("i",[10,20,30,40,50])

# function to add value in array 
arr.append(90)

# function to delete value from array 
arr.remove(90)

for index,value in enumerate(arr):
    print(f"array[{index}] -> {value}")