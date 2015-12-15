#!/usr/bin/python

import socket

# TODO only print when verbose variable is set or whatever
# TODO logging

class CSocketServer:

    def __init__(self, port=None):
        """
        Global constructor

        :param port: override port
        :return CSocketServer object
        """

        print("[CSocketServer] create socket.socket() object")

        # Create a socket object
        self.__socket = socket.socket()

        print("[CSocketServer] define params")

        # Define Params
        self.__host = "0.0.0.0"
        if port is not None:
            self.__port = port
        else:
            # use default port
            # TODO define as constant
            self.__port = 6615

        print("[CSocketServer] done; [host] %s [port] %s" % (self.__host, self.__port))

        self.__socket.bind((self.__host, self.__port))

        print("[CSocketServer] socket bound to host and port")


    def getSocket(self):
        """
        ....
        :return:
        """

        return self.__socket

