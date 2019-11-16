import sys
from .Tape import Tape
class BFInterpreter():
    def __init__(self):
        self.tape: Tape = Tape()
        self.loopStack = []
        self.program: str = ''
        self.programCounter: int = 0

    def loadProgram(self, program: str):
        self.program: str = program
        self.programCounter = 0
    
    def loadProgramFromFile(self, src_file):
        self.program = ''
        self.programCounter = 0
        with open(src_file, 'r') as source:
            for char in source.read():
                self.program += char

    def runProgram(self):
        self.programCounter = 0
        charDict: dict = {
            '>': self.tape.goRight,
            '<': self.tape.goLeft,
            '+': self.tape.increment,
            '-': self.tape.decrement,
            '.': self._handlePeriod,
            ',': self._handleComma,
            '[': self._handleLeftBracket,
            ']': self._handleRightBracket
        }
        while self.programCounter < len(self.program):
            curChar = self.program[self.programCounter]
            if curChar in charDict:
                charDict[curChar]()
            self.programCounter += 1

    def _handlePeriod(self):
        val = self.tape.read()
        print(chr(val), end='')

    def _handleComma(self):
        val = sys.stdin.buffer.read(1)[0]
        self.tape.write(val)

    def _handleLeftBracket(self):
        val = self.tape.read()
        if val == 0:
            while self.programCounter < len(self.program) and \
                    self.program[self.programCounter] != ']':
                self.programCounter += 1
        else:
            self.loopStack.append(self.programCounter)

    def _handleRightBracket(self):
        val = self.tape.read()
        if len(self.loopStack) < 1:
            raise Exception(f'Invalid brackets at char {self.programCounter}')
        if val == 0:
            self.loopStack.pop()
        else:
            self.programCounter = self.loopStack[-1]
    
    def printTape(self):
        print(self.tape)