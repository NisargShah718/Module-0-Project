def factorial(n):
    if n!=2:
        return n*factorial(n-1)
    else:
        return 2
print(factorial(3))
print(factorial(4))
print(factorial(999))