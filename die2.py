# imports the random package so you can call a random method that you may need to
# use in your class to select or create random data or results.
import random
#New Class created called Die. With two variables set at certain values, for my methods
# to run effectively. For example there is 6 sides to the dice and only 1 face can seen
# at any one time.
class Die:
    face_value = 1
    sides = 6
    # Function to show the current face of the dice
    def show (self):
          return  "(" +str(self.face_value)+")"
    # Gets the face value of the dice that is being shown.
    def getFaceValue(self):
            return self.face_value
    # Rolls the dice at randowm between numbers 1 to 6 as set in the variable
    # parameters above.
    def roll(self):
            self.face_value=random.randint(1, self.sides)
            

    # Sets the size of the dice so you can increase how many faces it has.
    def setSize (self, size):
        self.sides = size
    # Prints out what size you have previously set the dice to in the method above.0
    def getSize(self):
        return (self.sides)


# New function added to the class that uses all the previous functions pre-set within the
# class. This function is created so you can roll a 100 dice and see how many of each value]
# you have rolled starting with two variable arrays intialiated. 
def roll100dice ():
    # The first two variables set as counter arrays to be used in the program.
    diceList = []
    sideCount = []

    # This sets the dicelist range to 100 from class Die and sets its size to be
    # from 1 to 6.
    for i in range (0,100):
        diceList.append (Die())
        diceList[i].setSize(6)
        
    # sets a new variable to be used in the range that gets the size pre entered.
    num = diceList[0].getSize()
    # Sets the sidecount range as the amount of face values from the previous range of 100
    # that has been set up and allocating it to the sidecount array.
    for i in range (0,num):
        sideCount.append(0)
        
    # Sets the operation of rolling 100 dice that has been set in the range.
    for i in range (0,100):
        diceList[i].roll()
        
        
       
      # Sets the variable value to get all 100 faces and calulate how many of the ]
      # the number of values on each given face.
        value = diceList[i].getFaceValue()
        sideCount[value-1] += 1
        # returns the sidecount arrays with values included.
    return (sideCount) 
    
        
   
        

        
       
 
    
