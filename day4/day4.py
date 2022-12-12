def full_intersection(pairs):
    total = 0
    for pair in pairs:
        intervals = [[int(i) for i in pair[0].split(
            '-')], [int(j) for j in pair[1].split('-')]]
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        # S1 >= S2, E1 <= E2
        # S2 >= S1, E2 <= E1
        if sorted_intervals[0][0] >= sorted_intervals[1][0] and sorted_intervals[0][1] <= sorted_intervals[1][1] or sorted_intervals[1][0] >= sorted_intervals[0][0] and sorted_intervals[1][1] <= sorted_intervals[0][1]:
            total += 1
    return total


def intersection(pairs):
    total = 0
    for pair in pairs:
        intervals = [[int(i) for i in pair[0].split(
            '-')], [int(j) for j in pair[1].split('-')]]
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        if sorted_intervals[1][0] <= sorted_intervals[0][1]:
            total += 1
    return total


def get_lines(input_file_string):
    with open(input_file_string, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        pairs = [line.strip().split(',') for line in lines]
        if input_file_string == 'input1.txt':
            return full_intersection(pairs)
        else:
            return intersection(pairs)


print(get_lines('input1.txt'))
print(get_lines('input2.txt'))
