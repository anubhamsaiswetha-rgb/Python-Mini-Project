try:
    num1=int(input("enter a number: "))
    num2=int(input("enter a number "))
    print("choose operators: +,-,*,/")
    op=input(("enter operator: "))
    if op == "+":
        print("result:", num1 + num2)
    elif op == "-":
        print("result:", num1 - num2)
    elif op == "*":
        print("result:", num1*num2)
    elif op == "/":
        print ("result:", num1/num2)
    else:
        print("invalid operator")
except ZeroDivisionError:
    print("error:division cannot perform")
except ValueError:
    print("error:invalid input")
else:
    print("calculation succesful")
       