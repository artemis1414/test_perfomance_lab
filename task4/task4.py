import sys

file_nums = open(sys.argv[1], 'r', encoding='UTF-8')
list_nums = []
for line in file_nums.readlines():
    list_nums.append(int(line))
file_nums.close()
count = 0
med_num = round(sum(list_nums) / len(list_nums))
for number in list_nums:
    while number != med_num:
        if number > med_num:
            number -= 1
        elif number < med_num:
            number += 1
        count += 1

print(count)