my_list = [1, 2, 2, 3, 4, 4, 5]
my_list_2 = []
[my_list_2.append(number) for number in my_list if number not in my_list_2]
#my_list_2 = []
#for number in my_list:
 #   if number not in my_list_2:
  #      my_list_2.append(number)
print(my_list_2)