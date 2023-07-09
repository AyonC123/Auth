from os import path
import sys

args = sys.argv

# check if input & file exist
if not len(args) >= 2:
    print("No input file", file=sys.stderr)
elif not path.isfile(args[1]):
    print("File doesn't exist", file=sys.stderr)
else:
    # open the file
    with open(args[1], "r") as data:
        # read the file
        file = data.read()
        # variable storing chars at whicht the line end
        lines = [0]
        print(file)

        # function to find the line and char for the current number
        def findLine(number):
            if len(lines) == 1:
                return f"line: {len(lines)}; charector: {number + 1}"
            else:
                return f"line: {len(lines)}; charector: {number - lines[-1]}"

        # function to find a particular char
        def findChar(char, number):
            for i in range(len(file) - number):
                letter = number + i - 1
                if file[letter] != char:
                    continue
                else:
                    return letter

        # function to parse the file
        def parse():
            for char in range(len(file)):
                if file[char] == "\n":
                    lines.append(char)
                if file[char] == "<":
                    char += 1
                    match file[char]:
                        case "p":
                            print("p start")
                            char += 1
                            if file[char] != ">":
                                print(f"missing '>' at {findLine(char)}")
                                break
                            else:
                                print("p content")
                                char = findChar("<", char)
                                if file[char+1] != "/":
                                    print(f"missing '/' at {findLine(char)}")
                                else:
                                    char += 2

                                if file[char] != "p":
                                    print(f"missing 'p' at {findLine(char)}")
                                else:
                                    char += 1

                                if file[char] != ">":
                                    print(f"missing '>' at {findLine(char)}")
                                else:
                                    char += 1
                                    print('p end')

                        case "h":
                            print("heading")

        parse()
