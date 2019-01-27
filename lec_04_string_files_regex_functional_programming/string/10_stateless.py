result_list = []

while True:
    data = input()
    if data.lower() == 'collapse':
        for item in result_list:
            if len(item) == 0:
                print('(void)')
            else:
                print(item)
        break
    data_2 = input()
    while not len(data_2) == 0:
        data = data.replace(data_2, '')
        data_2 = data_2[1:-1]
    result_list.append(data)
