import os

class getInfoFilePC:
    def __init__(self):
        self.pathFilePC = '/home/vlalin/PycharmProjects/pc_os_sniffle/InfoPC/'
        self.data = []
    def infoFile(self):
        for files in os.listdir(self.pathFilePC):
            self.data.append(files)
        return self.data
