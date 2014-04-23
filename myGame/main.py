import myfile

print "****************************************"
print "* Welcome to the game world of Maxiee! *"
print "****************************************"

if myfile.isSaveExist():
    print "Now load the saving document..."
    data = myfile.readMySave()
    print "Welcome back, %s." % data['name']
else:
    print "It seems the first time you play this game..."
    print "Now we'll create a new profile for you..."
    print "What's your name?"
    myName = raw_input(">")
    print "Good! Hello %s. Let's dive into the world of Maxiee!" % myName
    data = {}
    data['name'] = myName
    myfile.updateMySave(data);

print "Boring unpromising graduate life..."
