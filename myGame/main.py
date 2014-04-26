import myfile
import player

print "****************************************"
print "* Welcome to the game world of Maxiee! *"
print "****************************************"

fileSave = myfile.FileSave()
myPlayer = player.Player()

if fileSave.isSaveExist():
    print "Now load the saving document..."
    data = fileSave.readMySave()
    print "Welcome back, %s." % data['name']
else:
    print "It seems the first time you play this game..."
    print "Now we'll create a new profile for you..."
    print "What's your name?"
    myPlayer.setName(raw_input(">"))
    print "Good! Hello %s. Let's dive into the world of Maxiee!" % myPlayer.getName()
    fileSave.updateMySave(myPlayer.getData());

print "Boring unpromising graduate life..."
