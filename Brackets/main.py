class Bracket:
    def __init__(self, brackets):
        self.brackets = brackets

    def is_true(self):
        while '()' in self.brackets:
            self.brackets = self.brackets.replace('()', '')
        return self.brackets

    def __str__(self):
        return 'True' if len(self.is_true()) == 0 else 'False'


user_input = Bracket(input())
print(user_input)
