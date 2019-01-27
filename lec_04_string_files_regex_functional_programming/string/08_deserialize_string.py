my_dict = {}
while True:
    data = input()
    if data == 'end':
        break
    for dd in list(map(int, data[2:].split('/'))):
        my_dict[dd] = data[0]
result = ''
for key, value in dict(sorted(my_dict.items())).items():
    result += value
print(result)
