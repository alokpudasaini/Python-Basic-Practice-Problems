n = int(input("Enter a number: "))
def recur_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recur_factorial(n-1)
if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print("The factorial of",n,"is",recur_factorial(n))