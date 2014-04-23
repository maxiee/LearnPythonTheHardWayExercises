from os import path
import pickle

saveDocPath = path.expandvars("$HOME/.config/myGameSaved.dat")

def isSaveExist():
    return path.exists(saveDocPath)

def readMySave():
    return pickle.load(open(saveDocPath))

def updateMySave(data):
    pickle.dump(data, open(saveDocPath, 'w'))
