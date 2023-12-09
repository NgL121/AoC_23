with open('input.txt', 'r') as data:
    lines = data.readlines()

    output = 0
    for line in lines:
        history = []
        line = [int(num) for num in line.split()]
        history.append(line[-1])

        temp = line

        while list(set(temp)) != [0]:
            curr_val = temp[0]
            if len(temp) == 1:
                while history[-1] != 0:
                    history.pop()
                break

            for idx, num in enumerate(temp):
                if idx == 0:
                    continue

                point = num - curr_val
                curr_val = num
                temp[idx] = point

                # end of a line
                if idx == len(temp) - 1:
                    history.append(point)

            temp.pop(0)
            curr_val = temp[0]

        output += sum(history)

    print(output)