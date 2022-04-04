import socket
import sys
import struct
import time
import random

localIP = "127.0.0.1"
localPort = 20002
bufferSize = 1024

# Create a datagram socket
UDP_RCVR = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDP_RCVR.bind((localIP, localPort))

# Set the socket option to limit the receive buffer to 64 bytes
UDP_RCVR.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,64)

# Print to show that the socket is ready to recieve
print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    time.sleep(0.009)
    bytesAddressPair = UDP_RCVR.recvfrom(bufferSize)
    msg = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(msg)
    msg_lng = struct.unpack('>i', msg[:4])[0]
    msg_unpk = struct.iter_unpack('>d', msg[4:])
    
    tmp_dt = []
    while True:
        try:
            tmp_dt.append(next(msg_unpk)[0])
            print(tmp_dt[-1])
        except StopIteration:
            break

    print(clientMsg)
    # print(clientIP)

