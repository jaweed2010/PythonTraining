n = int(input("Enter a num: "))
ans = True
if n == 1:
    ans = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            ans = False
            break
        i += 1
print(ans)
