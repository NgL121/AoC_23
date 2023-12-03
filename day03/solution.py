find = []
def horizontal_check(line, num_range):
    if num_range[0] > 0:
        if line[num_range[0] - 1] != '.':
            return True
    if num_range[1] < len(line):
        if line[num_range[1]] != '.':
            return True

    for char in line[num_range[0]:num_range[1]]:
        if (not char.isdigit()) and char != '.':
            return True

    return False

with open('input.txt', 'r') as data:
    data = [line.strip() for line in data.readlines()]

    output = 0

    for idx_line, line in enumerate(data):
        idx_num = 0
        while idx_num < len(line):
            num = line[idx_num]
            current_number = ''
            if num.isdigit():
                pointer = idx_num + 1
                current_number += num
                while pointer < len(line) and line[pointer].isdigit():
                    current_number += line[pointer]
                    pointer += 1
                if current_number:
                    num_range = [idx_num, idx_num + len(current_number)]
                    valid = []
                    left_right = horizontal_check(line, num_range)
                    valid.append(left_right)
                    if idx_line > 0:
                        check_up = horizontal_check(data[idx_line-1],num_range)
                        valid.append(check_up)
                    if idx_line < len(data) - 1:
                        check_down = horizontal_check(data[idx_line+1], num_range)
                        valid.append(check_down)
                    if True in valid:
                        find.append(int(current_number))
                        output += int(current_number)
                idx_num += len(current_number)
            else:
                idx_num += 1


    print(output)