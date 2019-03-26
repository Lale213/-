import requests
import socket
def init_ip():
    ip1 = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip1 = socket.gethostbyname_ex(socket.gethostname())[2]
    try:
        ip1 = ip1 [1]
    except IndexError:
        ip1 = ip1[0]
    s.close()
    return ip1
def Internet_ON():
    try:
        r = requests.get('http://216.58.192.142', auth=('user', 'pass'))
        r.status_code
        ip1 = init_ip()
        return ip1
    except OSError:
        return 0
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    Internet_ON()