import socket
import os
import getmac
import platform

from Client.Model.userNetworkData import userNetworkData


class DataPC_Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataPC_Singleton, cls).__new__(cls)
            hostname = socket.gethostname()
            cls.userNetworkData = userNetworkData(os.getlogin(), socket.gethostbyname(hostname),
                                                  getmac.get_mac_address(), platform.system(),
                                                  platform.release(), os.name)

        return cls.instance

    def getDataPC(self):
        return self.userNetworkData