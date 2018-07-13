import math
x = input("""This code will take a list of tuples each with two values. The purpose of this is to show the distance from the origin if the coords given as paramaters were represented on a standard cartesian coordinate plane. If a tuple was passed in with a value of (2,5)
that would be the same as saying a coordinate with an x value of 2 and y value of 5. An optional second argument is to list how many of the minimum values you would like to list (default is one). Please enter your desired list of tuples: """)
k = input("Please enter the number of closest coords you would like to display")
def closestToOrigin(coordSet, k = 1):
    if k >= len(coordSet):
        return "Please change number of closest coords you would like to display"
    lengths = {}
    for x in coordSet:
        lengths[(math.sqrt(x[0]**2 + x[1]**2))] = x
    Keys = [x for x in lengths]
    Keys.sort()
    return [lengths[x] for x in Keys][:k]
    
print(closestToOrigin(x))

spare = input("Press any key to exit")