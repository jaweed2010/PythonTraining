def print_positional_args(a, b, c, /):
    print(a)
    print(b)
    print(c)


print_positional_args(1, 2, 3)

'''
To specify that a function can have only positional arguments, add , / after the arguments
Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments
'''