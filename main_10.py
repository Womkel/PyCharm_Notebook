users = ["Brandon", "Emma", "Brian", "Sophia", "Bella", "Ethan", "Ava", "Benjamin", "Mia", "Chloe"]
#group = [x for x in users if x[0] == "B"]
#print(group)
group = []
for x in users:
    if x[0] == "B":
        group.append(x)
print(group)