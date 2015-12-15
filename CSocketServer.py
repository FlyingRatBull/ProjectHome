#!/usr/bin/python

import socket

class CSocketServer:

    # Create a socket object
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))

    s.listen(5)                 # Now wait for client connection.
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        c.send('Thank you for connecting')
        c.close()                # Close the connection
