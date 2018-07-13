length = input("""This program will find the index of a number in the fibonacci sequence minus 1. This was done simply to give the\nprogram its goal of: find the number of ways a frog can jump across a pond of n length and have jumps of 1 or 2 feet.\nPlease checkout brilliant.org for more information on this topic.\nNow, please enter the length of the pond(or index of fib sequence you wish to find + 1):""")
length = int(length)
def fib(n):    
    return fib(n-1) + fib(n-2) if n >= 2 else 1
print(fib(length))

input("Press any key to exit")