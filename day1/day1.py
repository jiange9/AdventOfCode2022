# import re

input1_str = "input1.txt"
input2_str = "input2.txt"


def find_most_calorie_elf(input_file_string):
    # Regex?????
    # f = open(inputFileString, 'r')
    # # print("output: ", f.read())
    # readF = f.read()
    # print(readF)
    # regSplit = re.split('(.+\r?\n)+(?=(\r?\n)?)', readF)
    # print(regSplit)

    # Dumb solution
    cur_max = 0
    with open(input_file_string, 'r') as f:
        lines = f.readlines()
        calories = [line.strip() for line in lines]
        cur_sum = 0
        for s in calories:
            if s == '':
                if cur_sum > cur_max:
                    cur_max = cur_sum
                cur_sum = 0
            else:
                cur_sum += int(s)
    return cur_max


def find_top_three_sum(input_file_string):
    calorie_sums = []
    with open(input_file_string, 'r') as f:
        lines = f.readlines()
        calories = [line.strip() for line in lines]
        cur_sum = 0
        for s in calories:
            if s == '':
                calorie_sums.append(cur_sum)
                cur_sum = 0
            else:
                cur_sum += int(s)
    calorie_sums.sort(reverse=True)
    return sum(calorie_sums[:3])


print(find_most_calorie_elf(input1_str))
print(find_most_calorie_elf(input2_str))
print(find_top_three_sum(input1_str))
print(find_top_three_sum(input2_str))
