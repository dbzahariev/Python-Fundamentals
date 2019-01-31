count = int(input())

my_list = []
my_dict = {}
# find_max_char = ''

for i in range(count):
    new_row = input()

    my_list.append(new_row)

    for letter in new_row:
        # if new_row.count(letter) == len(new_row):
        #     find_max_char = letter
        # else:
        if letter not in my_dict:
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1

count_max_char = 0
max_char = ''
for key, value in my_dict.items():
    if count_max_char < value:
        count_max_char = value
        max_char = key

# finded_row = []
# for row in my_list:
#     kk = ''
#     for letter in row:
#         if letter == find_max_char:
#             kk += letter
#     if kk is not '':
#         finded_row.append(kk)

# cc = 1
# for row in finded_row:
#     if cc <= len(row):
#         print(row)
#         cc += 2
# print(finded_row)


kk = 1
for i in range(int(len(my_list[0]) / 2) + 1):
    row = ''
    for i_2 in range(kk):
        row += max_char
    print(row)
    kk += 2
