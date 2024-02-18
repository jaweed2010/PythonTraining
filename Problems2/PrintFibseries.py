n = int(input("Enter number of terms: "))
fib = list()
if n == 1:
    fib.append(0)
elif n == 2:
    fib.append([0, 1])
else:
    fib = [0, 1]
    for i in range(n - 2):
        cur = fib[-1] + fib[-2]
        fib.append(cur)
print(fib)
