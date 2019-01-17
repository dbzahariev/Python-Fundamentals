my_dict = {}
target = ''
list_order = []


def is_float(this_value):
    try:
        float(this_value)
        return True
    except ValueError:
        return False


def is_int(this_value):
    try:
        int(this_value)
        return True
    except ValueError:
        return False


while True:
    entrance = input()
    if entrance == 'filter base':
        continue
    if entrance == 'Position' or entrance == 'Salary' or entrance == 'Age':
        target = entrance
        break
    entrance = entrance.split()
    entrance.remove('->')
    key = entrance[0]
    value = entrance[1]
    this_target = ''
    if is_int(value):
        # TODO: Ako trqbva go kovertirai na int
        this_target = 'Age'
    elif is_float(value):
        # TODO: Ako trqbva go kovertirai na float
        this_target = 'Salary'
    else:
        this_target = 'Position'
    if key in my_dict:
        my_dict[key][this_target] = value
    else:
        my_dict[key] = {this_target: value}
    list_order.append(key)
# print(my_dict)


# for dict_key, dict_value in my_dict.items():
#     for key, value in dict_value.items():
#         if key is not target:
#             my_dict[dict_key][key] = None
#             # del my_dict[dict_key][key]
#         # print(key)
#     # if target in value:

for name in list_order:
    key = name
    value = my_dict[key]
    if target in value:
        print(f'Name: {key}')
        print(f'{target}: {value[target]}')
        print(f'====================')

# TODO: Sortirai po vhod
