import sys
node = None
player_inventory = []
all_items = []

player_skills = []
all_skills = []

#Bug fixes for version 2: 
#Rooms now loop no more issues of rooms leading to same rooms
#Introduction to game so players don't feel lost
#ITALLICIZED TEXT
#small code fixes

class character(object):
    def __init__(self, attack_power=10, health=100, name = 'Bandit'):
        self.attack_power = attack_power
        self.health = health
        
class me(character):
    def __init__(self, attack_power = 10, health = 100, chakra = 100, stamina = 100):
        super(me, self).__init__(attack_power, health)
        self.chakra = chakra
        self. stamina = stamina

  #  def attack(self, target):
   #     target.take_damage(self.attack_power)
    #    if target.health <=0:
     #       return 'target dead'
      #      del target
       # else:
        #    return target.health
    
    def take_damage(self, amount):
        self.health = amount
        
bandit1 = character()

bandit2 = character()


lead_bandit = character(15, 120, 'Bandit King')

moon_ninja = character(15, 110, 'Moon Village Ninja')

sun_ninja = character(15, 110, 'Sun Village Ninja')

rogue_ninja = character(20, 125, 'Rogue Ninja')

player = me()

#def combat(self):
    
###############################################################################

class item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
class weapon(item):
    def __init__(self,name, description, damage):
        super(weapon, self).__init__(name, description)
        self.damage = damage
            
class throwing_weapon(weapon):
    def __init__(self, name = 'Kunai Knife', description = 'It\'s an average kunai knife, lightweight, dependable, and deadly.', damage = 15):
        super(throwing_weapon, self).__init__(name, description, damage)
            
    def throw(self, target):
        print 'You throw %s' % (self.name)
        print 'You inflict %s' % (self.damage)
            
        target.take_damage(self.damage)
        if target.health <=0:
            return 'target dead'
        else:
            return target.health     
    
shuriken = throwing_weapon('Shuriken', 'It\'s an average shuriken, sharpened for maximum damage.', 10)
    
class sword(weapon):
    def __init__(self, name = 'Kitana', description = 'It\'s a basic kitana, made of folded metal to do a lot of damage, while being lightwiehgt', damage = 10):
        super(sword,self).__init__(name, description, damage)
        
    def swing(self, target):
        print 'You swing %s' % (self.name)
        print 'You inflict %s' % (self.damage)
            
        target.take_damage(self.damage)
        if target.health <=0:
            return 'target dead'
        else:
            return target.health
    
    
    
class consumable(item):
    def __init__(self, name = 'Food Pills', description = 'It\'s a simple food pill made by local herbs.', healing_value = 10, restore_value = 0):
        super(consumable, self).__init__(name, description)
        self.healing_value = healing_value
        self.restore_value = restore_value
            
    def consume(self):
        print 'You consume %s' % (self.name)
        print 'You get healed for %s' % (self.healing_value)
        print 'Your chakra and stamina get restored for %s' % (self.restore_value)
    
chakra_candy = ('Chakra Candy', 'It\'s pieces of candy designed to refil your chakra.', 0, 10)
    
class clothing(item):
    def __init__(self, name = 'Moon Headband', description = 'A simple headband from the moon village, with a black band.', slot = 'Head'):
        super(clothing, self).__init__(name, description)
        self.slot = slot
            
    def put_on(self):
        print 'You put on %s on your %s' % (self.name) % (self.slot)
    
Sun_Headband = clothing('Sun Headband', 'A simple headband from the sun village, with a blue band', 'Head')
                    
class jutsu(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
class ninjutsu(jutsu):
    def __init__(self, name = 'Fire Ball', description = 'You take a mighty breath and create a giant ball of flames', damage = 10, chakra_cost = 5):
        super(ninjutsu, self).__init__(name, description)
        self.damage = damage
        self.chakra_cost = chakra_cost
            
    def cast(self, target):
        print 'You weave the signs and cast %s' % (self.name)
        print 'You deal %s damage' % (self.damage)
            
        target.take_damage(self.damage)
        if target.health <=0:
            return 'target dead'
        else:
            return target.health
                
air_bullets = ninjutsu('Air Bullets', 'You take a deep breathe and blow out 3 large gusts of air.', 15, 5)
raging_water = ninjutsu('Raging Water Jutsu', 'You gather chakra in your stoumach form water a spit it all out in one push.', 8, 5)
chidori = ninjutsu('Chidori', 'You gather chakra in your hand and form it into lightning and lunge towards your opponent.', 50, 35)
    

class taijutsu(jutsu):
    def __init__(self, name, description, damage = 10, stamina_cost = 10):
        super(taijutsu, self).__init__(name, description)
        self.damage = damage
        self.stamina_cost = stamina_cost
            
    def do(self, target):
        print 'You channel your strength and perform %s' % (self.name)
        print 'You deal %s damage' % (self.damage)
            
        target.take_damage(self.damage)
        if target.health <=0:
            return 'target dead'
        else:
            return target.health
                
Spinning_leaf_hurricane = ('Spinning leaf hurricane', 'You take a step back run forward and kick and spin in midair', 15)
thousand_hand_punch = ('Thousand hands punch', 'You clear your mind and throw punches so quickly your oppponent swears their are 1000 hands.', 20)
    
        
class genjutsu(jutsu):
    def __init__(self, name = 'False Death', description = 'You create a clone and fake your death, it will take your opponent to find out what happened.', duration = 3):
        super(genjutsu, self).__init__(name, description)
        self.duration = duration
            
    def cast(self):
        print 'You weave the signs and cast %s' % (self.name)
        print 'You stun your opponent for %s moves' % (self.duration)
            
class sagejutsu(jutsu):
    def __init__(self, name = 'Toad Sage Jutsu', description = 'You stand still, gather chakra around you, and awaken the toad sage within you', duration = 5):
        super(sagejutsu, self).__init__(name, description)
        self.duration = duration
            
    def cast(self):
        print 'You stand still and gather chakra and cast %s' % (self.name)
        print 'Your next %s moves will be stronger' % (self.name)

##############################################################################
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
Village1 = room('Sun Village', 'Pathway', 'warzone', 'Forest8', 'Forest4', None, None, 'This village seems to be on high alert however people still going about on their daily buisness.')
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

print "\x1B[3mWelcome, to the hidden forest.\x1B[23m"
print "\x1B[3mThis land is divided between two villages, the sun and moon village, which are locked in eturnal conflict.  You must pick a side in their war and lead them to victory.\x1B[23m"
print "\x1B[3mAlso their have been reports of an all powerful ninja that has been kidnapping bodies and killing village members.\x1B[23m"
print "\x1B[3mThis game uses north, south, east, west, up, and down directions. Type the directions you want to go.\x1b[23m"
print
print "Good luck and have fun!"
print


#\x1B[3m \x1B[23m

while True:
    print 'You\'re currently in ' + node.name
    print
    print node.description 
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
            
    #Interact function
    #if command in ['interact', 'i']: