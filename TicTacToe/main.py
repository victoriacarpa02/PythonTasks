class TicTacToe:
    def __init__(self):
        self.field = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.turn = -1

    def show(self):
        print('|'.join(self.field[0]))
        print('-' * 5)
        print('|'.join(self.field[1]))
        print('-' * 5)
        print('|'.join(self.field[2]))

    def mark(self, n, m):
        if self.winner() is None:
            self.turn += 1
            sym = 'X' if self.turn % 2 == 0 else 'O'
            if self.field[n-1][m-1] not in ('X', 'O'):
                self.field[n-1][m-1] = sym
            else:
                print('Inaccessible cell')
                self.turn -= 1
        else:
            print('Game is over')

    def winner(self):
        # если совпало горизонтально
        for i in range(3):
            if ''.join(self.field[i]) in ('XXX', 'OOO'):
                return self.field[i][0]

        # если совпало вертикально
        for i in range(3):
            s = ''
            for j in range(3):
                s += self.field[j][i]
            if s in ('XXX', 'OOO'):
                return self.field[0][i]

        # если совпало по диагонали слева направо
        s = ''
        for i in range(3):
            s += self.field[i][i]
        if s in ('XXX', 'OOO'):
            return self.field[0][0]

        # если совпало по диагонали справа налево
        s = ''
        for i in range(3, 1, -1):
            s += self.field[i-1][i-1]
        if s in ('XXX', 'OOO'):
            return self.field[2][2]

        # если ничья
        r = []
        for el in self.field:
            r.append(True) if ' ' not in el else r.append(False)
        if all(r):
            return 'Draw'

        return None


tictactoe = TicTacToe()
