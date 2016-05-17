#Create a a class caled 'enemy'
#They should have a health and attack
#Create a function that removes health from an enemy
#Create a function that attacks a specified target
#It should return the damage dealt
#It should reduce the health of the target

class character(object):
    def __init__(self, attack_power=10, health=100):
        self.attack_power = attack_power
        self.health = health
        
class me(character):
    def __init__(self, attack_power = 10, health = 100, chakra = 100, stamina = 100):
        super(me, self).__init__(attack_power, health)
        self.chakra = chakra
        self. stamina = stamina

    #def attack(self, target):
        #target.take_damage(self.attack_power)
        #if target.health <=0:
            #return 'target dead'
            #del target
        #else:
            #return target.health
    
    def take_damage(self, amount):
        self.health = amount
        
bandit1 = character()

bandit2 = character()

player = me()

def combat():
    #
        #
    #
        #
    return 'ok'
    
    #if health == 0:
        #return 'Dead'
    #else:
        #return 'Not dead'