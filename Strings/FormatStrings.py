a = 10.0
b = 20
name = "ramu"

print(name, "has", a, "apples and", b, "bananas")

print("{} has {} apples and {} bananas".format(name, a, b))

print("{2} has {1} apples and {0} bananas".format(name, a, b))

print("%s has %d apples and %d bananas"%(name, a, b))

print(f"{name} has {int(a)} apples and {b} bananas")
