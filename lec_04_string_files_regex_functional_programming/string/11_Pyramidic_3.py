data = int(input())

my_list = []
my_dict = {}

for i in range(data):
    new_row = input()
    my_list.append(new_row)
    for letter in new_row:
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1

count_max_char = 0
count_max_char_in_row = 0
max_char = ''
for key, value in my_dict.items():
    if count_max_char < value:
        count_max_char = value
        max_char = key

for index in range(len(my_list)):
    for vv in my_list[index]:
        if vv is not max_char:
            my_list[index] = my_list[index].replace(vv, '')

        count_max_char_in_row = max(len(my_list[index]), count_max_char_in_row)

for count_chars_in_row in range(1, count_max_char_in_row + 1, 2):
    print(max_char * count_chars_in_row)
