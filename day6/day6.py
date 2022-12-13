def find_first_marker(s, delimiter):
    marker = 0
    unique_char = []
    while len(unique_char) != delimiter:
        for i in range(marker, len(s)):
            if s[i] not in unique_char:
                unique_char.append(s[i])
            elif s[i] in unique_char:  # Reset unique char and set
                unique_char = []
                marker += 1
                break
            # Dumb lol
            if len(unique_char) == delimiter:
                break
    return marker + delimiter


def get_lines(input_file_string):
    with open(input_file_string, 'r', encoding='utf-8') as f:
        line = f.readlines()
        print(find_first_marker(line[0], 4))
        print(find_first_marker(line[0], 14))


get_lines('input1.txt')
get_lines('input2.txt')
get_lines('input3.txt')
get_lines('input4.txt')
get_lines('input5.txt')
get_lines('input6.txt')
