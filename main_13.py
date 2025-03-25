products = ["Water", "Chocolate", "Chips", "Soda", "Sandwich"]
choice_index = int(input())
try:
    print(products[choice_index])
except IndexError:
    print("Wrong index")
finally:
    print("Need Help? Contact us")