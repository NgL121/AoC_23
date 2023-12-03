import re

with open('input.txt', 'r') as input:
    data = input.readlines()

    pattern = r'(\d)'
    output = 0

    for line in data:
        curr = ''
        match = re.findall(pattern, line)
        if not match:
            continue
        else:
            if len(match) > 1:
                curr += match[0] + match[-1]
            else:
                curr += match[0]*2
        output += int(curr)

print(output)
