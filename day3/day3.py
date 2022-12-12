from string import ascii_lowercase
from string import ascii_uppercase

priority_dict = {}


def construct_priority_dict():
    for priority, l in enumerate(ascii_lowercase, start=1):
        priority_dict[l] = priority

    for priority, u in enumerate(ascii_uppercase, start=27):
        priority_dict[u] = priority

    return priority_dict


def get_priority_sum(compartments, priority_dict):
    total = 0
    for compartment in compartments:
        first_half, second_half = compartment[:len(
            compartment)//2], compartment[len(compartment)//2:]

        total += priority_dict[find_common_character(first_half, second_half)]
    return total


def get_new_priority_sum(triplets, priority_dict):
    total = 0
    for triplet in triplets:
        first = find_common_character(triplet[0], triplet[1])
        second = find_common_character(first, triplet[2])
        total += priority_dict[second]
    return total


def find_common_character(first_half, second_half):
    d = {}
    common = ''
    for c in first_half:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in second_half:
        if c in d:
            d[c] -= 1
            if c not in common:
                common += c
    return common


def get_lines(input_file_string):
    priority_dict = construct_priority_dict()
    if input_file_string == 'input1.txt':
        with open(input_file_string, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            compartments = [line.strip() for line in lines]
            return (get_priority_sum(compartments, priority_dict))
    else:
        with open(input_file_string, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            triplets = [line.strip() for line in lines]
            triplets = [triplets[i * 3:(i + 1) * 3]
                        for i in range((len(triplets) + 3 - 1) // 3)]
            return (get_new_priority_sum(triplets, priority_dict))


print(get_lines('input1.txt'))
print(get_lines('input2.txt'))
