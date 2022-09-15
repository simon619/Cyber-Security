import threading
import nmap
import ipaddress
import re

port_pattern = re.compile("([0-9]+)-([0-9]+)")
valid_min, valid_max = 0, 65535
min_port, max_port = valid_min, valid_max
queue = []
open_ports = []  
thread_list = [] 
nm = nmap.PortScanner() 

while True:
    input_ip = input('Enter IP Address: ')
    try:
        valid_ip = ipaddress.ip_address(input_ip)
        print("Accepted IP Address")
        break
    except:
        print("Wrong IP Address")

while True:
    input_port = input("Enter Port in [min]-[max] Format and Minimum Difference Between Max and Min Must bo 100: ")
    valid_port = port_pattern.search(input_port.replace(" ",""))
    min_port, max_port = int(valid_port.group(1)),  int(valid_port.group(2))
    differ = max_port - min_port
    if valid_port and differ >= 100 :
        print('Port valid')
        break

def fill_port_queue(port_list):
    global queue
    queue = [port for port in port_list]

def nmap_scanner(port):
    global input_ip, open_ports
    try:
        result = nm.scan(input_ip, str(port))
        port_status = (result['scan'][input_ip]['tcp'][port]['state'])
        print(f'Port: {port} is {port_status}')
        if port_status == 'open':
            open_ports.append(port)
    except:
        print(f"Cannot scan port {port}.")

def process():
    global queue
    while queue:
        port = queue.pop(0)
        nmap_scanner(port)

port_list = range(min_port, max_port)
fill_port_queue(port_list)

for th in range(100):
    thread = threading.Thread(target=process)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(f'Opened Ports are {open_ports}')

