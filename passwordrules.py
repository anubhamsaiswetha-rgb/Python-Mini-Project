password=input("enter the password: ")
if len(password)<7:
    raise Exception ("invalid password")
else:
    print("correct password")