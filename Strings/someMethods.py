txt = "banana"

x = txt.center(20)

print(x)
##############################
txt = "My name is Ståle"

x = txt.encode(encoding="utf-8")

print(x)
##############################
# check if a certain phrase or character is present in a string
txt = "The best things in life are free!"
print("free" in txt)

# check if a certain phrase or character is NOT present in a string
txt = "The best things in life are free!"
print("expensive" not in txt)