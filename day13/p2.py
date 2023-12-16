class Pattern:
    def __init__(self, list_of_string):
        self.rows = list_of_string
        self.cols = self.get_col()

    def get_col(self):
        output =[]
        for idx_col in range(len(self.rows[0])):
            curr = ''
            for row in self.rows:
                curr += row[idx_col]
            output.append(curr)
        return output

    def get_refl_val(self):
        output = 0

        col, stat_col = check_refl(self.cols)
        row, stat_row = check_refl(self.rows)

        if stat_col > 0 and stat_row == 0:
            output += col
        elif stat_col == 0 and stat_row > col:
            output += row * 100
        else:
            output += row * 100

        return output

def count_diff(str1, str2):
    count = 0

    for i, char in enumerate(str1):
        if char != str2[i]:
            count += 1

    return count

def check_refl(list_of_string):
    temp = 0

    for idx, char in enumerate(list_of_string[:-1]):
        valid = False

        if count_diff(char, list_of_string[idx + 1]) <= 1:
            output = idx + 1
            l = idx
            r = idx + 1

            while l >= 0 and r < len(list_of_string):
                left = list_of_string[l]
                right = list_of_string[r]

                if left != right:
                    if count_diff(left, right) == 1:
                        l -= 1
                        r+= 1
                        valid = True
                        continue

                    else:
                        output = 0
                        break

                l -= 1
                r += 1

            if l == -1 or r == len(list_of_string):
                if not valid:
                    temp = output
                else:
                    return output, 1
    if temp > 0:
        return temp, 0

    return 0, 0

with open('input.txt', 'r') as data:
    patterns = [pattern.strip() for pattern in data.read().split('\n\n')]

    patterns_list = []

    for patt in patterns:
        patterns_list.append(Pattern(patt.split('\n')))

    output = 0
    for p in patterns_list:
        output += p.get_refl_val()

    print(output)