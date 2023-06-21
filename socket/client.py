import socket
import json


def test(args):
    print(args)


funcs = {"test": test}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 55555))
    data = json.loads(s.recv(1024).decode("ascii"))
    funcs[data["function"]](data["args"])
    while True:
        message = input("> ").encode("ascii")
        s.send(message)
