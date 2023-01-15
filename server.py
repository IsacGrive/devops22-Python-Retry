import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6061))
s.listen(2)


def greeting():
    print(f'SERVER: Server greets {name}')


class status():

    def conn_status(connection):
        if connection == 1:
            return ('Server now has connection')
        if connection == 2:
            return ('No connection')


print(status.conn_status(connection=2))
clientSocket, address = s.accept()
print(f'Connection established from adress: {address}')
name = clientSocket.recv(1024).decode()
greetings = 'Hello ' + name
clientSocket.send(greetings.encode())
greeting()
print(status.conn_status(connection=1))


def server_commands():
    if data == 'hej server':
        clientSocket.send(f'Hej {name}'.encode())
    if data == 'ping':
        clientSocket.send('pong'.encode())
    if data == 'whoami':
        clientSocket.send(f'{name}'.encode())
    if data == 'bye':
        s.close()


while True:
    data = clientSocket.recv(1024).decode()
    if not data:
        break
    server_commands()
