import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 55555))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            nickname = nicknames[index]
            clients.remove(client)
            client.close()
            broadcast(f'{nickname} has left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break


def recieve():
    client, address = server.accept()
    print(f'connected with {str(address)}')

    client.send(b'NICK')
    nickname = client.recv(1024).decode('ascii')
    clients.append(client)
    nicknames.append(nickname)

    print(f'Nickname of this client is {nickname}')
    broadcast(f'{nickname} joined the chat!'.encode('ascii'))
    client.send(b'Connected to the server')

    print(nicknames, clients)

    thread = threading.Thread(target=handle, args=(client,), daemon=True)
    thread.run()
    print("hi")


print('Server is listening...')
while True:
    recieve()
