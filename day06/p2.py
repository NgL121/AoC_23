import math

with open('input.txt', 'r') as data:
    lines = [line.strip() for line in data.readlines()]

    time = lines[0]
    time = ''.join(time.split(':')[1].split())
    time = int(time)


    distance = lines[1]
    distance = int(''.join(distance.split(':')[1].split()))

    delta = time**2 - 4*distance

    found = [(time - math.sqrt(delta))//2, (time + math.sqrt(delta))//2]

    print(int(found[1] - found[0]))