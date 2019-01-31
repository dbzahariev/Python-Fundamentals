data = input()

while data != "end":
    borderFirst = data[0:round(len(data) / 2)]
    borderSecond = ''
    border = ''

    if len(data) % 2 == 0:
        borderSecond = data[len(borderFirst):len(data) - len(borderFirst)]
    else:
        borderSecond = data[len(borderFirst) + 1:len(data) - len(borderFirst) - 1]

    while True:
        if borderFirst == borderSecond:
            border = borderFirst
            break
        elif borderFirst != borderSecond:
            borderFirst = borderFirst[len(borderFirst) - 1:]
            borderSecond = borderSecond.Substring(1, len(borderSecond) - 1)

        if len(borderFirst) == 0 and len(borderSecond) == 0:
            break

    if len(border) != 0:
        core = data[:len(data) - len(border)] + data[len(data) - len(border) + len(border.strip())]
        # core = core.Remove(0, len(border)).Trim()
        core = core[len(border.strip()):]
        if core != "":
            nilapdromes = core + border + core
            print(nilapdromes)

    data = input()
