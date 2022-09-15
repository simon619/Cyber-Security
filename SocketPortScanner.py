import threading
import socket

target = '192.168.0.1'
open_port = []
queue = []

def port_scanner(port):
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((target, port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.append(port)

def worker():
    while queue:
        port = queue.pop(0)
        if port_scanner(port):
            print(f'Port {port} is open!')
            open_port.append(port)

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []
n = 100 # Increment n to incease speed

for th in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(f'Open Ports are {open_port}')

