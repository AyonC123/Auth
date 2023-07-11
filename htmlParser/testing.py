string = """
<p widht=\"100vw\" height=\"100vh\" color=\"black\">hello</p>
<p widht=\"100vw\" height=\"100vh\" color=\"black\">hello</p>
<p        width="100 vh" height= "1760vw"    ></p>
<p        width=100 height=1760    ></p>
<span color="black"></span>
"""

i = 0
while i < len(string):
    if string[i] == "<":
        i += 1
        tag = ""
        closingTag = ""
        args = ""
        value = ""
        while string[i] != " ":
            tag += string[i]
            i += 1
        while string[i] != ">":
            args += string[i]
            i += 1
        i += 1
        while string[i] != "<":
            value += string[i]
            i += 1
        i += 1
        if string[i] != "/":
            print("error")
        i += 1
        while string[i] != ">":
            closingTag += string[i]
            i += 1
        if tag != closingTag:
            print("error")
        print(f"tag: {tag}; args: {args.strip()}; value: {value};")

    i += 1
