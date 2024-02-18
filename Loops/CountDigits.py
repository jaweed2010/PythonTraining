n = int(input("Enter the number: "))
digits = 0
while n > 0:
    digits += 1
    n = n // 10
print(digits)
