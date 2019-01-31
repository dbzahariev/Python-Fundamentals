count = int(input())


def detect_char(this_row):
    this_row = list(this_row)
    kk = ''
    this_count = 0
    for char in this_row:
        if this_count <= this_row.count(char):
            this_count = this_row.count(char)
            kk = char

    return [kk, this_count]


def return_chars(this_row, finddd):
    this_row = list(this_row)
    kk = ''
    for char in this_row:
        if char == finddd:
            kk += finddd
    return kk


def find_max_char():
    one_max_char = ''
    count_max_char = 0
    for char_pair in finded_char_list:
        if count_max_char <= char_pair[1]:
            one_max_char = char_pair[0]
            count_max_char = char_pair[1]
    return [one_max_char, count_max_char]


def return_all_chars_in_row(this_row, char):
    kk = ''
    for letter in this_row:
        if letter == char:
            kk += char
    return kk


finded_char_list = []
my_list = []
for n in range(count):
    new_row = input()
    my_list.append(new_row)
    finded_char_list.append(detect_char(new_row))

founded_max_char = find_max_char()[0]
founded_max_char_count = find_max_char()[1]

for row in my_list:
    print(return_all_chars_in_row(row, founded_max_char))
