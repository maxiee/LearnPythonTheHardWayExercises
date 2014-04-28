from sys import exit

class Scene(object):

    def enter(self):
        print "This scene is not yet configured."
        print "SubClass it and implement enter()."
        exit(1)

class Office(Scene):
    
    def enter(self):
        print "Location: Office"
        print "What do you want:"
        print "\t1. Pomodoro"
        print "\t2. rest for 5 mins"
        print "\t3. Go to finace ministry"
        print "\t4. exit"
        input = raw_input("> ")
        while input != "4":
            if input == "1":
                print "Pomodoro is comming soon..."
            elif input == "2":
                print "Ok, now rest for 5 minutes..."
            # we can add a function in scene class
            # to wrap the welcome words and the user switch
            elif input == "3":
                return "finance_ministry"
            input = raw_input("> ")
        return 'office'

class FinanceMinistry(Scene):

    def enter(self):
        print "Finace Ministry is building..."
        print "Don't warried. It's usefuless for you anyway..."
        return 'office'

class Map(object):

    scenes = {
            'office': Office(),
            'finance_ministry': FinanceMinistry()
            }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
