age = int(input("Enter you age: "))
is_student = False
if age < 18:
    if is_student:
        print("20% discount")
    else:
        print("10% discount")
else:
    print("Regular price")
