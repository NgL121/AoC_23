def hash_function(string):
    current_point = 0
    for char in string:
        current_point += ord(char)
        current_point *= 17
        current_point %= 256
    return current_point


string_with_length = {}
box = {i : [] for i in range(256)}

with open('input.txt', 'r') as data:
    codes = data.readline().split(',')
    output = 0

    for string in codes:
        if string.endswith('-'):
            string = string[:-1]
            pos = hash_function(string)
            if string in box[pos]:
                box[pos].pop(box[pos].index(string))

        else:
            string = string.split('=')
            pos = hash_function(string[0])
            string_with_length[string[0]] = int(string[1])
            if string[0] not in box[pos]:
                box[pos].append(string[0])

    output = 0
    for string in string_with_length:
        pos = hash_function(string)
        if string in box[pos]:
            pos = hash_function(string)
            output += ((pos + 1) * (box[pos].index(string) + 1) * string_with_length[string])

    print(output)