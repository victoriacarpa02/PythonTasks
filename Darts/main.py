class Darts:
    def __init__(self, size):
        self.size = size

    def matrix(self):
        return [[0]*self.size for _ in range(self.size)]

    def to_darts(self):
        max_el, min_el = self.size-1, 0
        number = 1
        res = self.matrix()
        while min_el <= max_el:
            for i in range(len(res)):
                for j in range(len(res)):
                    if res[i][j] == 0 and (i == min_el or j == max_el or j == min_el or i == max_el):
                        res[i][j] = number
            number += 1
            max_el -= 1
            min_el += 1
        return res

    def __str__(self):
        res = []
        matrix = self.to_darts()
        for row in matrix:
            res.append(' '.join(str(x) for x in row))
        return '\n'.join(x for x in res)


x = Darts(int(input()))
print(x)
