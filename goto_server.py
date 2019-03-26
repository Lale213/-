import time
import socket
import Error_Massage
def Reg(Person):
    Person.insert(0,'Regist')
    sock=socket.socket()
    sock.connect(('192.168.43.216',9090))
    for row in Person:
        temp = bytes(row, 'utf-8')
        sock.send(temp)
        time.sleep(0.3)
    time.sleep(1)
    data = sock.recv(1024)
    sock.close()
    print(data)
    data = data.decode('utf-8')
    print(data)
    if(data == '111111no'):
        Error_Massage.ERROR(6)
    elif(data != '111111fine'):
        Error_Massage.ERROR(5)
    elif(data == '111111fine'):
        return 1

def Init(User):
    User.insert(0, 'Enter')
    sock = socket.socket()
    sock.connect(('192.168.43.216', 9090))
    for row in Person:
        temp = bytes(row, 'utf-8')
        sock.send(temp)
        time.sleep(0.3)
    time.sleep(1)
    data = sock.recv(1024)
    sock.close()
    print(data)
    data = data.decode('utf-8')
    print(data)
    if (data == '111no'):
        Error_Massage.ERROR(6)
    elif (data != '111fine'):
        Error_Massage.ERROR(5)
    elif (data == '111fine'):
        return 1


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    Person = ('13asd123','qazwsx123', 'Var', '')
    Reg(Person)  # то запускаем функцию main()