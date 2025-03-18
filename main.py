password = "Secret"
enter_password = input("Enter your password: ")
while password != enter_password:
    print("Try again")
    enter_password = input()
print ("Welcome")