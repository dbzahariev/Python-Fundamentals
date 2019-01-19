def sum_adj_nums(numbers):
    adj_exist = True
    while adj_exist:
        temp_list = []
        for i in range(0, len(numbers) - 1):
            first_num = numbers[i]
            second_num = numbers[i + 1]
            if first_num == second_num:
                third = first_num + second_num
                numbers[i] = third
                numbers.pop(i + 1)
                break
            if i == len(numbers) - 2:
                return numbers
        for num in numbers:
            temp_list.append(num)
        numbers.clear()
        for num in temp_list:
            numbers.append(num)

        if len(numbers) == 1:
            return numbers


def print_nums(final_nums):
    for i in range(0, len(final_nums)):
        if final_nums[i] % 1 == 0:
            final_nums[i] = int(final_nums[i])
    return print(*final_nums, sep=' ')


nums = list(map(float, input().split(' ')))
result = sum_adj_nums(nums)
print_nums(result)
