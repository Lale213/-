import socket, threading

class ClientThread(threading.Thread):
    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip=ip
        self.port=port
        self.socket = socket
        print('[+] New thread started for ' + ip+ ':' + str(port))

    def run(self):
        print('Connection from:' + ip+':'+ str(port))
        clientsock.send('\nWelcome to the server\n\n')
        data = 'dummydata'
        while len(data):
            data = clientsock.send('You sent me ' + data)
        print('Client disconnected...')
host = '0.0.0.0'
port = 9090

tcpsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((host,port))
threads = []

while True:
    tcpsock.listen(4)
    print('\nListening for incoming conne ctions...')
    (clientsock, (ip,port)) = tcpsock.accept()
    newthread = ClientThread(ip,port, clientsock)
    newthread.start()
    threads.append(newthread)
for t in threads:
    t.join()










def manypotok()
    while 1:
        s = socket.socket()
        s.bind(('',9090))
        s.listen(1)
        conn, addr = s.accept()
        print('connected:', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        conn.close()
























