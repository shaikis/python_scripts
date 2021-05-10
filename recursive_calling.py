def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x -1))

n = 20

print("Factorial of  ", n, " is ",  factorial(n))