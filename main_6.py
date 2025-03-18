def rect(leight, width):
    area = leight * width
    perimetr = 2 * leight + 2 * width
    price = 1000 * area
    return area, perimetr, price
x, y, e = rect(50, 100)
print(x, y, e)