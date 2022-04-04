import socket
import sys
import struct
import time
import random

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

#Print that he socket is ready
print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    time.sleep(0.009)
    # Sending a reply to client
    bytesToSend = struct.pack(">d", 1)
    bytesToSend += struct.pack(">d", 2)
    bytesToSend += struct.pack(">d", 9)
    bytesToSend += struct.pack(">d", 5)
    UDPServerSocket.sendto(bytesToSend, ('127.0.0.1', 20002))
