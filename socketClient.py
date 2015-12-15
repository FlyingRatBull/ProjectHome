#!/usr/bin/python

"""
Simple test script for socket server
"""

# TODO command line tool for socketClient


import socket

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 6615                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when donee