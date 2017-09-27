import random
snap = False

while snap==False:
    card1 = (random.randrange(1,10))
    card2 = (random.randrange(1,10))
    if card1==card2:
        print("SNAP!")
        print("Cards were " + str(card1) + ", " + str(card2))
 
        snap = True
    else:
        print("Unlucky! " + str(card1) + " : " + str(card2))
    
        
