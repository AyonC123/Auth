import socket
import threading

nickname = input('Choose a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occoured!")
            client.close()
            break


def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('ascii'))


recieveThread = threading.Thread(target=recieve)
recieveThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()
