import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 55555))
    s.listen()
    print("Server listening")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        conn.sendall(b"{\"function\": \"test\", \"args\": \"hello\"}")
