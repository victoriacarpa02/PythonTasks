from sys import stdin
import re


class Coordinates:
    def __init__(self, data):
        self.data = [line.strip() for line in data]
        self.result = [re.findall(r'-?\d+\.?\d*', line) for line in self.data]

    def is_true_coordinates(self):
        res = []
        for line in self.result:
            res.append('True' if -90 <= float(line[0]) <= 90 and -180 <= float(line[1]) <= 180 else 'False')
        return res

    def __str__(self):
        return '\n'.join(self.is_true_coordinates())


user_input = Coordinates(stdin)
print(user_input)
