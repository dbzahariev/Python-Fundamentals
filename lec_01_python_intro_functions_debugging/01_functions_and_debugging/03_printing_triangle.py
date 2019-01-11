n = int(input())


def create_line(k):
    kk = ''
    for i in range(1, k + 1):
        kk += f'{i} '
    return kk


def first_part_print():
    for a in range(1, n + 1):
        line = create_line(a)
        print(line)


def second_part_print():
    for a in range(n - 1, 0, -1):
        line = create_line(a)
        print(line)


first_part_print()
second_part_print()
