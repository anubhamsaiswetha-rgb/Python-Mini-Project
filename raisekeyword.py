age=int(input("enter age: "))
if age <18:
    raise Exception("Not eligible")
print("Eligible")