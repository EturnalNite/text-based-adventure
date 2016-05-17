import random
import sys



class Fight(object):
  def enter(self):
    print "\n", "-" * 10
    print "There is a muchacho, he is about 8 years old and is crying:"
    print "Enemy: MUCHACHO"
    print "Clean Version"

    your_hit_points = 20
    muchacho1_hit_points = 50
    muchacho1 = True
    health_p = random.randint(0,4)
    epotion = random.randint(0,2)
    your_attack = random.randint(3,7)
    muchacho1_attack = random.randint(1,6)


    play_stat = raw_input("Would you like to play with stats, Yes or no?: ")
    
    if play_stat == "Yes":
        zz = raw_input("You have a skill point, what would you like to invest in, Attack, Defense or Luck?: ")
        if zz == "Attack":
            your_attack += 2
           
        if zz == "Defense":    
            your_hit_points += 5

        if zz == "Luck":
            health_p +=1
        
   
    
    print "You have %d health potions" %health_p  

    while your_hit_points > 0 and (muchacho1):
      print "\n", "-" * 10
      c = raw_input("Do you wanna 1:Slash or 2:Stab or 3:Use Health Potion? :")
      a = ["1","2"]
      b = random.choice(a)
        

      if c ==  "Quit":
        print "Goodbye"
        sys.exit(0)
       
            
      if  c == "3":
          if health_p >0:  
            your_hit_points +=10
            health_p -=1
            print "You get health cause ya had  potions, you have %d health" %your_hit_points
            
          else:
              print "Ya got no potions"
     
      if c==b:
        if muchacho1:
          muchacho1_hit_points = muchacho1_hit_points - your_attack
          print "You hit MUCHACHO1 for %d hit points, it causes the child to cry even more, he death will be soon.  " % your_attack
          print "He has %d health left." %muchacho1_hit_points 
        
          if your_attack == 7:
            print "You did critical damage!"

        
          
          if muchacho1_hit_points <5:
             if epotion>0: 
              print "He used a health potion, that bastard, he has health" 
              muchacho1_hit_points += 15
              epotion -=1
              print  "He has %d health points" %muchacho1_hit_points
          else:
              print " "
        
          
          
          if muchacho1_hit_points <= 0:
            muchacho1 = False
            
            print "MUCHACHO was killed, you stand over the beaten, bloody corpse of an 8 year old! You laugh as his body rots."
            print "You had %d health left" %your_hit_points


      if c!=b:
        your_hit_points = your_hit_points - muchacho1_attack
        
        if your_hit_points - muchacho1_attack and not c == "3":
            print "You missed!!!"
        
        print ("MUCHACHO1 hits you for %d points, you have %d hit points, your pathetic, a child hurt you"
           %(muchacho1_attack, your_hit_points))
        
        
        if your_hit_points>3 and your_hit_points<10:
            print "Ya hurt real bad kid"
        
        if your_hit_points <= 0:
          print 'You are dead, your are a worthless piece of crap'
          break
      
a_fight = Fight()
a_fight.enter()
