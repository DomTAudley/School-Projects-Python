import random

print("SIMPLE GAME OF SNAP!")
print("====================");      
#set loop condition to false
snap = False

#create array of cards
deckOfCards = ["1","2","3","4","5","6","7","8","9","10","jack","queen","king"]
lengthOfArray = len(deckOfCards)

while snap==False:

    #get element from the array using the randrange and len to determine the array size
    card1 = deckOfCards[random.randrange(0, lengthOfArray)]

    #get element from the array using the randrange and len to determine the array size
    card2 = deckOfCards[random.randrange(0, lengthOfArray)]

    #check if snap
    if card1==card2:
        print("**********")
        print("** SNAP **")
        print("**********")
        print("Cards were " + card1 + " and " + card2)
 
        snap = True
    else:
        print("Unlucky :( Cards were " + card1 + " and " + card2)
    
        
