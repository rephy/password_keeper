from random import *

class RandomPassword:

    def __init__(self):
        self.password = ""
        self.num_letters = randint(0, 8)
        self.num_digits = randint(2, 4)
        self.num_symbols = randint(2, 4)

        self.letters = [letter for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
        self.numbers = [str(num) for num in range(9)]
        self.symbols = [symbol for symbol in '!@#$%^&*()']

        self.generate_password()

    def generate_password(self):
        temp_list = []

        for n in range(self.num_letters):
            rand_letter = choice(self.letters)
            temp_list.append(rand_letter)

        for n in range(self.num_digits):
            rand_digit = choice(self.numbers)
            temp_list.append(rand_digit)

        for n in range(self.num_symbols):
            rand_symbol = choice(self.symbols)
            temp_list.append(rand_symbol)

        shuffle(temp_list)

        for char in temp_list:
            self.password += char