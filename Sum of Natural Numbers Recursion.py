n = int(input("Enter the number of terms: "))
def recur_sum(n):
    if n<=1:
        return n
    else:
        return n + recur_sum(n-1)
print("The sum is",recur_sum(n))