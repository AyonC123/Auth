string = """
<p widht=\"100vw\" height=\"100vh\" color=\"black\">hello</p>
<p widht=\"100vw\" height=\"100vh\" color=\"black\">hello</p>
<p        width="100 vh" height= "1760vw"    ></p>
<p        width=100 height=1760    ></p>
<span color="black"></span>
<span>sdfasdf<p>dfd</p>dfadf<a></a></span>
"""


def parse(index=0, oneOnly=False):
    i = index
    while i < len(string):
        closingTag = ""
        tag = ""
        args = ""
        value = ""
        if string[i] == "<":
            i += 1
            g = i
            try:
                while string[i] != " ":
                    tag += string[i]
                    i += 1
                while string[i] != ">":
                    args += string[i]
                    i += 1
            except:
                i = g
                tag = ""
                args = ""
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
                    payload = parse(index=i, oneOnly=True)
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
            print(f"tag: {tag}; args: {args.strip()}; value: {value};")

        i += 1
        if oneOnly:
            return [i, f"[tag: {tag}; args: {args.strip()}; value: {value};]"]


parse()
