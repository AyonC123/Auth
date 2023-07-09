from os import path
import sys

args = sys.argv

if not len(args) >= 2:
    print("No input file", file=sys.stderr)
elif not path.isfile(args[1]):
    print("File doesn't exist", file=sys.stderr)
else:
    with open(args[1], "r") as data:
        file = data.read()
        lines = [0]
        print(file)

        def findLine(number):
            if len(lines) == 1:
                return f"line: {len(lines)}; charector: {number + 1}"
            else:
                return f"line: {len(lines)}; charector: {number - lines[-1]}"

        def findChar(char, number):
            for i in range(len(file) - number):
                letter = number + i - 1
                if file[letter] != char:
                    continue
                else:
                    return letter

        def parse():
            for i in range(len(file)):
                if file[i] == "\n":
                    lines.append(i)
                if file[i] == "<":
                    i += 1
                    match file[i]:
                        case "p":
                            print("p start")
                            i += 1
                            if file[i] != ">":
                                print(f"missing '>' at {findLine(i)}")
                                break
                            else:
                                print("p content")
                                i = findChar("<", i)
                                if file[i+1] != "/":
                                    print(f"missing '/' at {findLine(i)}")
                                else:
                                    i += 2

                                if file[i] != "p":
                                    print(f"missing '/' at {findLine(i)}")
                                else:
                                    i += 1

                                if file[i] != ">":
                                    print(f"missing '/' at {findLine(i)}")
                                else:
                                    i += 1
                                    print('p end')

                        case "h":
                            print("heading")

        parse()
