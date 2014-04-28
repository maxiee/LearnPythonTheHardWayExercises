import myfile
import player
import mymap

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        
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

        while(True):
            print "Boring unpromising graduate life..."
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

the_map = mymap.Map('office')

the_game = Engine(the_map)

the_game.play()
