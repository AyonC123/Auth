string = "<p widht=\"100vw\" height=\"100vh\" color=\"black\">hello</p>"

i = 0
while i < len(string):
    if string[i] == "<":
        i += 1
        match string[i]:
            case "p":
                args = ""
                value = ""
                tag = ""
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
                    tag += string[i]
                    i += 1
                if tag != "p":
                    print("error")
                print(f"tag: {tag}; args: {args}; value: {value};")

    i += 1
