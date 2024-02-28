def addn(a, b):
    return a + b


def sub(a, b):
    return a - b


def arith(func):
    a = func(10, 20)
    print("a: ", a)


arith(addn)
arith(sub)
