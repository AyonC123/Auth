from os import path
import sys

args = sys.argv


def parse(string, index=0, oneOnly=False):
    i = index
    while i < len(string):
        closingTag = ""
        tag = ""
        args = ""
        value = ""
        finalArgs = ""
        if string[i] == "<":
            i += 1
            g = i
            try:
                while string[i] != " ":
                    tag += string[i]
                    i += 1
                i += 1
                while string[i] != ">":
                    args += string[i]
                    i += 1
                j = 0
                while j < len(args):
                    if args[j] != "=":
                        finalArgs += args[j]
                        finalArgs.strip()
                    else:
                        finalArgs += args[j]
                        finalArgs.strip()
                    j += 1
            except:
                i = g
                tag = ""
                args = ""
                finalArgs = ""
                while string[i] != ">":
                    tag += string[i]
                    i += 1

            i += 1

            def parseNested(i, string):
                value = ""
                while string[i] != "<":
                    value += string[i]
                    i += 1
                i += 1
                if string[i] != "/":
                    i -= 1
                    payload = parse(string, index=i, oneOnly=True)
                    i = payload[0]  # type: ignore
                    value += payload[1]  # type: ignore

                    data = parseNested(i, string)
                    value += data[0]
                    i = data[1]
                return [value, i]
            data = parseNested(i, string)
            value += data[0]
            i = data[1]

            i += 1
            while string[i] != ">":
                closingTag += string[i]
                i += 1
            if tag != closingTag:
                print("error")
            if not oneOnly:
                print(f"tag: {tag}; args: {finalArgs}; value: {value};")

        i += 1
        if oneOnly:
            return [i, f"[tag: {tag}; args: {finalArgs}; value: {value};]"]


if not len(args) >= 2:
    print("No input file", file=sys.stderr)
elif not path.isfile(args[1]):
    print("File doesn't exist", file=sys.stderr)
else:
    with open(args[1], "r") as data:
        # read the file
        parse(data.read())
        # variable storing chars at whicht the line end
