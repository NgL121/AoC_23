import re

with open('input.txt', 'r') as input:
    data = input.readlines()

    valid = {'one': '1',
             'two': '2',
             'three' : '3',
             'four' : '4',
             'five' : '5',
             'six' : '6',
             'seven' : '7',
             'eight' : '8',
             'nine' : '9'}

    pattern = '(?=('

    for num in valid:
        pattern += num + '|'

    pattern += '\d))'
    output = 0

    for line in data:
        curr = ''
        matches = [re.findall(pattern, line)[0], re.findall(pattern, line)[-1]]
        for match in matches:
            if match in valid:
                curr += valid[match]
            else:
                curr += match

        output += int(curr)

print(output)
