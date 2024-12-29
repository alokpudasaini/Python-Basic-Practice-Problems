n = int(input("Enter the number of terms: "))
def Fibo(n):
    if n<=1:
        return n
    else:
        return (Fibo(n-1) + Fibo(n-2))
print("Fibonacci sequence: ")
for i in range(n):
    print(Fibo(i))