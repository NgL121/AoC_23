import re

red_lim = 12
green_lim = 13
blue_lim = 14

with open('input.txt', 'r') as input:
    data = input.readlines()

    ids_pattern = r'Game (\d+):'
    blue_pattern = r'(\d+) blue'
    red_pattern = r'(\d+) red'
    green_pattern = r'(\d+) green'

    p1 = 0
    p2 = 0

    for line in data:
        valid = True
        ids = int(re.findall(ids_pattern,line)[0])
        red = max([int(num) for num in re.findall(red_pattern, line)])
        green = max([int(num) for num in re.findall(green_pattern, line)])
        blue = max([int(num) for num in re.findall(blue_pattern, line)])
        if red > red_lim or green > green_lim or blue > blue_lim:
            valid = False
        if valid:
            p1 += ids
        p2 += red * green * blue

    print(p1)
    print(p2)