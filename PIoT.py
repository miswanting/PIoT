# coding=utf-8
import socket

import lib_Net.lib_Net

DEFAULT_PORT = 8765


class PIoT(object):
    """docstring for PIoT."""

    def __init__(self, debug=False):
        super(PIoT, self).__init__()
        self.debug = debug
        net = lib_Net.lib_Net.Cloud()
        print(net.getMyIP())

if __name__ == '__main__':
    PIoT(True)
