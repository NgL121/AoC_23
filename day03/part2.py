def check(line, idx):
    output = []
    left_pointer = idx - 1
    right_pointer = idx + 1

    if not line[idx].isdigit():
        curr_num = ''
        while left_pointer >= 0 and line[left_pointer].isdigit():
            curr_num = line[left_pointer] + curr_num
            left_pointer -= 1
        if curr_num:
            output.append(int(curr_num))

        curr_num = ''
        while right_pointer < len(line) and line[right_pointer].isdigit():
            curr_num += line[right_pointer]
            right_pointer += 1
        if curr_num:
            output.append(int(curr_num))
    else:
        curr_num = line[idx]
        while left_pointer >= 0 and line[left_pointer].isdigit():
            curr_num = line[left_pointer] + curr_num
            left_pointer -= 1
        while right_pointer < len(line) and line[right_pointer].isdigit():
            curr_num += line[right_pointer]
            right_pointer += 1
        if curr_num:
            output.append(int(curr_num))

    return output

count = 0

with open('input.txt', 'r') as data:
    data = [line.strip() for line in data.readlines()]

    output = 0

    for idx_line, line in enumerate(data):
        for idx_symbol, symbol in enumerate(line):
            num_list = []
            if symbol == '*':
                num_list += check(line, idx_symbol)
                if idx_line > 0:
                    num_list += check(data[idx_line - 1], idx_symbol)
                if idx_line < len(data) - 1:
                    num_list += check(data[idx_line + 1], idx_symbol)

            if len(num_list) == 2:
                output += (num_list[0] * num_list[1])

    print(output)
