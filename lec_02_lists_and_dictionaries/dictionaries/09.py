n = int(input())
my_dict = {}
for i in range(n):
    pair = input().split(' -> ')
    color = pair[0]
    items = pair[1].split(',')
    new_items = {}
    for item in items:
        new_items[item] = items.count(item)
    if color not in my_dict:
        my_dict[color] = new_items
    else:
        new_list_items = my_dict[color]
        for i in new_items:
            if i in my_dict[color]:
                print(my_dict[color][i])
                my_dict[color][i] = my_dict[color][i] + 1
            else:
                my_dict[color][i] = 1

for key, value in my_dict.items():
    print(f'{key} clothes:')
    for item in value:
        print(f'* {item} - {my_dict[key][item]}')
# TODO: Add logic for Found!
