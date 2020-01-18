"""
    Script showing how to get keypresses for every key pressed
"""
import pyxhook
import socket
import sys
import time
import pickle
import numpy as np


HOST, PORT = "localhost", 9999

def OnKeyPress(event):
    data = event.Key
    data = pickle.dumps(data)
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(data)

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("Sent: {}".format(data))


hm = pyxhook.HookManager()
hm.KeyDown = OnKeyPress
hm.HookKeyboard()
hm.start()
