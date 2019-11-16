import argparse
from .BFInterpreter import BFInterpreter

if __name__ == "__main__":
    interpreter = BFInterpreter()

    parser = argparse.ArgumentParser(
        description='Run BF code from a file or the command line.')
    parser.add_argument('file', nargs='?',
        metavar='source.bf', type=str, help='File with bf source code', default=None)
    parser.add_argument('--cmd', metavar='bfstring', type=str, help='BF string')
    
    args = parser.parse_args()
    if args.file:
        interpreter.loadProgramFromFile(args.file)
    elif args.cmd:
        interpreter.loadProgram(args.cmd)
    else:
        raise Exception('No file or cmd specified.')

    interpreter.runProgram()