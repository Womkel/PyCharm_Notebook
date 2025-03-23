sports = ["Football", "Basketball", "Tennis", "Golf", "Volleyball"]
group = []
for x in sports:
    if "ball" in x:
        group.append(x)
# Или можно так
#group = [x for x in sports if "ball" in x]
print(group)