with open('input.txt', 'r') as data:
    codes = data.readline().split(',')

    output = 0
    for string in codes:
        current_point = 0
        for char in string:
            current_point += ord(char)
            current_point*= 17
            current_point %=256

        output += current_point

    print(output)