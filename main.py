import socket
import os 
import threading
from datetime import datetime
from colorama import Fore
import pyfiglet
import colorama
os.system(f'cls' if {os.name} == 'nt' else 'clear')

print(colorama.Fore.RED)
pyfiglet.print_figlet("Asylum")
print(colorama.Fore.GREEN)
print("             Port Scanner")
print(colorama.Fore.RESET)
target = input("Enter The IP==> ")




print('-'*41)
print('Scanning: ' + target)
print('Time Started: ' + str(datetime.now()))
print('-'*41)

ports = []

def scan(port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    try:
        connection.connect((target, port))
        connection.close()
        print(f'{Fore.WHITE}Port {Fore.RED}[{port}]{Fore.WHITE} is open')
        ports.append(port)
    except Exception:
        pass
scanned = 0
for port in range(1, 65500):
    thread = threading.Thread(target=scan, kwargs={'port': port})
    thread.start()
    scanned += 1

print(f'{scanned} ports were scanned')
print('open ports: ' + Fore.GREEN + str(ports))#  
