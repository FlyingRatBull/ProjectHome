from CSocketServer import CSocketServer

# TODO create CSocketServer object and let it listen
# TODO logging

print("[socketServer] get socket from CSocketServer")

# create socket object
mySocket = CSocketServer().getSocket()

print("[socketServer] listen to socket")

# Now wait for client connection.
mySocket.listen(5)

print("[socketServer] ")

while True:

    print("[socketServer] ")

    # Establish connection with client.
    # TODO use whitelist for acceptable clients?
    conn, addr = mySocket.accept()

    print("Got connection from: ", addr)

    conn.send("Thank you for connecting")

    print("[socketServer] ")

    # Close the connection
    conn.close()


