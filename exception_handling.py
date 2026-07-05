while True:
    try:
        x = int(input("Please enter a number: "))
        print(x)
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        

while True:
    try:
        dividend = float(input("Enter the dividend:"))
        divisor = float(input("Enter the diviser:"))
        quotient = dividend/divisor
        print("The quotient is:",quotient)
        break
    except ValueError:
        print("Enter valid number(s).")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")



