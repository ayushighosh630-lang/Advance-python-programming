
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


print("Fibonacci Number Calculator")
print("---------------------------")

n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative number.")

else:
    result = fibonacci(n)
    print("The", n, "th Fibonacci number is:", result)