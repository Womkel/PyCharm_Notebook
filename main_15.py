#price = int(input())
#if price != 500:
#    raise ValueError("Price 500")
#print("Good job")


#temp = -15
#if temp > 50 or temp < -10:
#    raise ValueError("Invalid range")

try:
    print(3 + "3")
except ValueError:
    print("Cannot add different types")
except TypeError:
    print("Type mismatch error")