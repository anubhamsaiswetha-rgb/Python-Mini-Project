try:
    f=open("sample.txt", "w")
    f.write("Hello Python")
except Exception:
    print("Error while writing file")
finally:
    f.close()
    print("file closed sucessfully")

