import sys
node = None

class room:
    def __init__(self, name, n_path, s_path, w_path, e_path, u_path, d_path, description):
        self.name = name
        self.north = n_path
        self.south = s_path
        self.west = w_path
        self.east = e_path
        self.up = u_path
        self.down = d_path
        self.description = description
        
    def move(self,direction):
        global node
        node = globals()[getattr(self,direction)]
        

    #I need an interact function
    def interact():
        #
        print 'place holder'

Destroyed_forest = room('Destroyed Forest', None, 'Pathway', 'Dead_bodies', 'Destroyed_village', None, None, 'You are standing in a forest, trees are knocked over, the ground is overturned, and you stand in the middle of a giant crater.')
Pathway = room('Start of trail', 'Destroyed_forest', 'Village1', 'Forest6', 'Forest1', None, None, 'A pathway leads to the south, it seems pretty barren, but it looks like it leads to a village.')
Dead_bodies = room('Pile of dead bodies', None, 'Forest6', None, 'Destroyed_forest', None, None, 'You stand in front of a pile of dead bodies of a whole bunch of ninjas, you could probably find some useful tools or some cool masks in the pile.')
Forest6 = room('Forest', 'Dead_bodies', 'Forest7', None, 'Village1', None, None, 'You stand in a plain looking forest, the whole forest looks pretty untouched.')
Forest7 = room('Forest', 'Forest6', 'Forest8', None, 'Village1', None, None, 'You stand in a pretty plain forest, the whole east side of the forest seems to have been used.')
Forest8 = room('Forest', 'Forest7', 'Shack', None, 'Fork', None, None, 'The forest has a path that leads to the east, but you feel like the heavens are trying to guide you to the south.')
Fork = room('A fork in the road', 'warzone', 'Village2', 'Forest8', None, None, None, 'Theres a fork in the road you can go north which looks like it leads to a warzone, and the south looks like it leads to a village.')
Village1 = room('Sun Village', 'Village1', 'Village2', 'Forest8', 'Forest4', None, None, 'You stand in a battlefield, ninjas from either side constantly watch you, dead bodies litter the ground, and traps cover up the floor.')
Village2 = room('Moon Village', 'warzone', None, 'Forest8', 'Forest5', None, None, 'You stand in a very busy village, everyone seems to be running around, security is on high alert, and every shop seems to be closed.')
Destroyed_village = room('Destroyed Village', None, 'Forest2', 'Destroyed_forest', 'Forest1', None, None, 'You stand at the edge of a destroyed village, there are bodies on the floor, burned buildings, and the gate is knocked over.')
Forest1 = room('Forest', None, 'Bandit_camp', 'Destroyed_village', None, None, None, 'A densely packed forest surrounds you, there are slight trails leading to the south.')
Bandit_camp = room('A Bandit Encampment', 'Forest1', None, 'Forest2', None, None, 'Hidden_cave', 'You stand at the edge of a campsite, some mean looking bandits sit around the fire, they sit near a ravine.')
Hidden_cave = room('A cave in the ravine', None, None, None, None, 'Bandit_camp', 'Cavern', 'As you head down the ravine, you enter a cave hidden behind some vines and some rocks it is dark, cold, and wet, it continues leading downward.')
Cavern = room('A cavern', None, None, None, None, 'Hidden_cave', 'Akastuki_hideout', 'You stand in the middle of a cavern at the end of the room a giant rock blocks a pathway.')
Akastuki_hideout = room('An Akastuki Hideout', None, None, None, None, 'Cavern', None, 'You stand in a room dimly let room you sense nothing, but blood lust, on the walls hang bloodied ninja tools.')
Forest2 = room('Forest', 'Destroyed_village', 'Forest3', 'Pathway', 'Bandit_camp', None, None, 'You stand in a plain, almost untouched forest.')
Forest3 = room('Forest', 'Forest2', 'Forest4', 'Village1', None, None, None, 'This forest seems like it is constantly used, to the west their seems to be a village of people.')
Forest4 = room('Forest', 'Forest3', 'Forest5', 'warzone', None, None, None, 'The forest seems pretty untouched, but the west side of the forest seems pretty destroyed.')
Forest5 = room('Forest', 'Forest4', None, 'Village2', None, None, None, 'The forest seeems to stretch endlessy to the south, but to the west theres a village.')
Shack = room('Old Dude\'s Shack', 'Forest8', None, None, None, None, None, 'You stand in a clearing at the forest, their is a shack an old man is standing in front of, he looks at you and screams out of excitement. This seems like an important place.')
warzone = room('A warzone', 'Village1', 'Village2', 'Forest8', 'Forest4', None, None, 'You stand in a battlefield ninjas from either side constantly watch you, dead bodies litter the ground, and traps cover up the floor.')

node = Destroyed_forest

while True:
    print 'room: ' + node.name
    print
    print 'Description: ' + node.description 
    print
    
    command = raw_input('>').strip().lower()
    movement = ['north','south','east','west','up','down']
    if command in ['q', 'quit', 'exit']:
        print 'You commit seppuku.'
        sys.exit(0)
    if command in movement:
        try:
            node.move(command)
        except:
            print 'You can\'t go that way, without the season pass.'
    else:
        print 'I don\'t understand that command.'