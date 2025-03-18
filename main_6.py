def rect(leight, width):
    area = leight * width
    perimetr = 2 * leight + 2 * width
    return area, perimetr
x, y = rect(50, 100)
print(x, y)