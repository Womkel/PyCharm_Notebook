def minimal(l):
    minimal_number = l[0]
    for el in l:
        if el < minimal_number:
            minimal_number = el
    return minimal_number

nums_1 = [1, 2, 5, 8, 0.6, -2]
min_1 = minimal(nums_1)

nums_2 = [0, -1, 2, 0.5]
min_2 = minimal(nums_2)

if min_1 < min_2:
    print("First lower: ", min_1)
else:
    print("Second lower: ", min_2)