def calc_area(a, b):
    return (a * b) / 2


a = float(input())
b = float(input())

area = calc_area(a, b)
print(f'{area:.12g}')
