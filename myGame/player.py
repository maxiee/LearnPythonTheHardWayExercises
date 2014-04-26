class Player(object):
    def __init__(self):
        self.data = {}

    def setName(self, name):
        self.data['name'] = name

    def getName(self):
        if self.data.has_key('name'):
            return self.data['name']
        else:
            return 'Name not set yet!'

    def getData(self):
        return self.data
