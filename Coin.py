import random

class Coin:
    # This class lets us create Coin objects
    showing_heads=True # By default the coin shows "heads"
    value=1# By default the coin has the value 1p
    
    def show(self):
        # Returns a string to incicate which face of the coin is showing
        if (self.showing_heads==True):
            return "Heads"
        else:
            return "Tails"

    def turn(self):
        # Turns the coin over
        self.showing_heads=not self.showing_heads
        
    def setValue (self,coinVal):
        # Sets value of the coin
        self.value = coinVal
        
    
    def getValue (self):
        # Returns set value of coin
        print (self.value)

    def flip(self):
        # Flips over coin at random.
        self.showing_heads=random.choice([True,False])

def threeMatches():
    # Sets variable loop to true to call the loop method.
        loop=True
        #Creates the 3 coin objects to be flipped.
        coin1=Coin()
        coin2=Coin()
        coin3=Coin()
        # Sets up the method in the while loop for the action from when the user presses
        # the enter button.
        while (loop):
         coinchange = input('enter')
         if coinchange =="":
         #Prints the faces of the 3 coins before they are flipped.
          print (coin1.show())
          print (coin2.show())
          print (coin3.show())
         
         # Flips all 3 coins over then shows the new faces.
          coin1.flip()
          coin2.flip()
          coin3.flip()
        
       
        
       
        # If statement that states if all three coins match it will print an all three match message and stop the program.
          if coin1.showing_heads==coin2.showing_heads==coin3.showing_heads:
              return "All three match"
           
          else:
              loop
        
coin1 = Coin ()


            

