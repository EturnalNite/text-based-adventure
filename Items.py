#This is Areg's Code Please thank him for his dank code
execfile("C:\\Users\\9hf3\\Desktop\\Project\\enemy program.py")

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

chakra_candy = ('Chakra Candy', 'It\'s pieces of cnady designed to refil your chakra.', 0, 10)

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
            
air_bullets = ninjutsu(' ', ' ', 15, 5)

class taijutsu(jutsu):
    def __init__(self, name, description, damage = 10):
        super(taijutsu, self).__init__(name, description)
        self.damage = damage
        
    def do(self, target):
        print 'You channel your strength and %s' % (self.name)
        print 'You deal %s damage' % (self.damage)
        
        target.take_damage(self.damage)
        if target.health <=0:
            return 'target dead'
        else:
            return target.health
            
Spinning_leaf_hurricane = ('Spinning leaf hurricane', 'You take a step back run forward and kick and spin in midair', 15)
    
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