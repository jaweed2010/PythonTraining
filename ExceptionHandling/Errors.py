def calculate():
    try:
        num1 = int(input("Enter first number"))
        num2 = int(input("Enter second number"))
        sum = num1 + num2
        diff = num1 - num2
        prod = num1 * num2
        div = num1 / num2
    except ZeroDivisionError:
        print("Division by zero")

    except ValueError:
        print("invalid input")

    else:
        print(f"No error occurred. sum is {sum}. Diff is {diff}. prod is {prod}. div is {div}")
    finally:
        print("Calculations are done")


calculate()
