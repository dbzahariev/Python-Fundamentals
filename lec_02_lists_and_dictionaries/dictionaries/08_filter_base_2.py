my_list = []
target = ''


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
    try:
        value = int(value)
        this_target = 'Age'
    except:
        try:
            value = float(value)
            this_target = 'Salary'
        except:
            this_target = 'Position'
    # if value % 1 == 0:
    #     this_target = 'Age'
    #     value = int(float(value))
    # elif value % 1 != 0:
    #     this_target = 'Salary'
    #     value = float(value)
    # else:
    #     this_target = 'Position'
    my_list.append([key, this_target, value])

for row in my_list:
    if target == row[1]:
        print(f'Name: {row[0]}')
        print(f'{row[1]}: {row[2]}')
        print(f'====================')
