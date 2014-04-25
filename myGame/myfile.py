from os import path
import pickle

class FileSave(object):
    saveDocPath = path.expandvars("$HOME/.config/myGameSaved.dat")

    def isSaveExist(self):
        return path.exists(self.saveDocPath)

    def readMySave(self):
        return pickle.load(open(self.saveDocPath))

    def updateMySave(self, data):
        pickle.dump(data, open(self.saveDocPath, 'w'))
