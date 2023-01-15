import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),6060))

name =input('Enter your name: ')
s.send(name.encode())

while True:
    data= s.recv(1024).decode()
    print(f'SERVER: {data}')

    msg=input('Enter message:')
    s.send(msg.encode())
    if msg == 'bye':
        try:
            print('--SERVER SHUTDOWN!--')
            break
            
        except OSError as e:
            print(e)

        s.close()
    
