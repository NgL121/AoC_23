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
        if check_refl(self.cols) > check_refl(self.rows):
            output += check_refl(self.cols)
        else:
            output += check_refl(self.rows) * 100
        return output

def check_refl(list_of_string):
    for idx, char in enumerate(list_of_string[:-1]):

        if char == list_of_string[idx + 1]:
            output = idx + 1
            l = idx
            r = idx + 1

            while l >= 0 and r < len(list_of_string):
                left = list_of_string[l]
                right = list_of_string[r]

                if left != right:
                    output = 0
                    break

                l -= 1
                r += 1

            if l == -1 or r == len(list_of_string):
                return output

    return 0


with open('input.txt', 'r') as data:
    patterns = [pattern.strip() for pattern in data.read().split('\n\n')]

    patterns_list = []

    for patt in patterns:
        patterns_list.append(Pattern(patt.split('\n')))

    output = 0
    for p in patterns_list:
        output += p.get_refl_val()

    print(output)