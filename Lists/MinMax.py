# With built-in function
li = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
print("min =", min(li))
print("max=", max(li))

# Without built-in function
li = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
min_li = float('inf')
max_li = float('-inf')
for i in li:
    if i < min_li:
        min_li = i
    if i > max_li:
        max_li = i
print("min=", min_li)
print("max=", max_li)
