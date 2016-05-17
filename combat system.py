class character(object):
    def __init__(self, attack_power=10, health=100, name = 'Bandit'):
        self.attack_power = attack_power
        self.health = health
        
class me(character):
    def __init__(self, attack_power = 10, health = 100, chakra = 100, stamina = 100):
        super(me, self).__init__(attack_power, health)
        self.chakra = chakra
        self. stamina = stamina

    def attack(self, target):
        target.take_damage(self.attack_power)
        if target.health <=0:
            return 'target dead'
        else:
            return target.health
    
    def take_damage(self, amount):
        self.health -= amount
        
bandit1 = character()

bandit2 = character()

moon_ninja = character(15, 110, 'Moon Village Ninja')

sun_ninja = character(15, 110, 'Sun Village Ninja')

rogue_ninja = character(20, 125, 'Rogue Ninja')