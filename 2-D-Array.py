
# declare an 2-D Array

twoDArray = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# print 2-D Array using nested for loop

# this loop will get Row
for x in twoDArray:
    print("[",end="")
# this loop will get Column 
    for y in x:
        print(f"{y}",end=" ")
    print("]")
