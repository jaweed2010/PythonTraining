# With built-in function
li = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
li.reverse()
print(li)

# Without built-in function
li = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
rev_li = list()
for i in li[::-1]:
    rev_li.append(i)
print(rev_li)
