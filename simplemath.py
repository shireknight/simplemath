import sys, os
import random

class App():
    # $$ indicates properties
    # all other vars indicated with $
    name = ''
    right_answers = 0

    def __init__(self):
        if not self.name:
            self.name = raw_input('Enter your name: ')
        hello = 'Hello ' + self.name + ', Would you like to try a math problem? (y, n): '
        read = raw_input(hello)
        self.start(read)


    def start(self, read):
        if read == 'y':
            self.stepTwo()
        elif read == 'n':
            sys.exit()
        else:
            # recursively call the app constructor if none of the above
            App()

    def stepTwo(self):
        read = 'Would you like to try addition or subtraction? (+, -): '
        sign = raw_input(read)
        if sign == '+' or sign == '-':
            self.mkEquation(sign)
        else:
            # if not + or - recursively call the function
            self.stepTwo()


    def mkEquation(self, sign):
        randa = random.randrange(1, 100)
        if sign == '+':
            randb = random.randrange(1, 100)
            equation = str(randa) + ' + ' + str(randb) + ' = '
            isum = randa + randb;
        if sign == '-':
            randb = random.randrange(1, randa)
            isum = randa - randb;

        equation = str(randa) + ' ' + sign + ' ' + str(randb) + ' = '
        answer = raw_input(equation)
        self.evalAnswer(int(answer), isum)



    def evalAnswer(self, answer, isum):
        while answer != isum:
            if answer < isum:
                answer = raw_input('Too low! Try again: ')
            if answer > isum:
                answer = raw_input('Too high! Try again: ')

        self.right_answers += 1;
        correct = 'Correct! '
        tally = self.name + ', you have answered ' + str(self.right_answers) + ' problems correctly!'
        print correct + ' ' + tally
        read = raw_input('Would you like to try another?: ')
        self.start(read)

if __name__ == "__main__":
  App()
