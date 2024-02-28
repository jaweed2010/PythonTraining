addn = lambda a, b: a + b
print(addn(10, 20))

sub = lambda a, b: a - b
print(sub(10, 20))

prod = lambda a, b: a * b
print(prod(10, 20))

################################


li = [1, 2, 3, 4, 5]
add2 = list(map(lambda x: x + 2, li))
print(add2)
even = list(filter(lambda x: x % 2 == 0, li))
print(even)

