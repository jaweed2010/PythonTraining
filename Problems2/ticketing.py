age = int(input("Enter age: "))
gender = input("Enter gender: ")
price = "Ticket price is "
# For senior citizens
if age >= 60:
    if gender == "M":
        price += str(40)
    else:
        price += str(35)
# For adults
elif age >= 18:
    if gender == "M":
        price += str(50)
    else:
        price += str(45)
# for kids/teens
else:
    price += str(10)
print(price)
