import myfile

print "****************************************"
print "* Welcome to the game world of Maxiee! *"
print "****************************************"

if myfile.isSaveExist():
    print "Now load the saving document..."
    savedDocument = open("save.dat")
    myName = savedDocument.readline().strip()
    print "Welcome back, %s." % myName
else:
    print "It seems the first time you play this game..."
    savedDocument = open("save.dat",'w')
    print "Now we'll create a new profile for you..."
    print "What's your name?"
    myName = raw_input(">")
    print "Good! Hello %s. Let's dive into the world of Maxiee!" % myName
    savedDocument.write(myName + '\n')

print "Boring unpromising graduate life..."
