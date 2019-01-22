my_dict = {}


def is_contains(search, search_in):
    if len(search) > len(search_in):
        return False
    for index in range(len(search)):
        if search[index] not in search_in:
            return False
    return True


def add_prefix(prefix, this_list):
    for index in range(len(this_list)):
        this_list[index] = f'{prefix}{this_list[index]}'
    return this_list


while True:
    internal = input()
    if internal.lower() == 'filter':
        target_topic = input().split(', ')
        for key, value in my_dict.items():
            if len(value) > 0 and is_contains(target_topic, value):
                value = add_prefix('#', value)
                print(f"{key} | {', '.join(value)}")
        break
    pair = internal.split(' -> ')
    key = pair[0]
    values = pair[1].split(', ')
    if key not in my_dict:
        my_dict[key] = []

    for value in values:
        if value not in my_dict[key]:
            my_dict[key].append(value)
