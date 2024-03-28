def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


f1 = open("input_EvenOdd")
file_string = (f1.read())
for x in file_string:
    print(check_even_odd(int(x)))

