class Lift:
    def __init__(self, enterPeople: int, currentFloor: int, destinationFloor: int, maxPeople = 11, maxFloor = 18):
        self.enterPeople = enterPeople
        self.currentFloor = currentFloor
        self.maxPeople = maxPeople
        self.destinationFloor = destinationFloor
        self.maxFloor = maxFloor
  
    def openDoor(self, currentPeople):
        if (currentPeople + self.enterPeople <= self.maxPeople):
            print('Lift doors are closing and good to go')
            Lift.moveUpOrDown(self)
        else:
            print('Lift is full; alarm rings and doors stay open')
    
    def moveUpOrDown(self):
        if self.destinationFloor == self.currentFloor:
            print('You are already on the floor #{}, bodoh.'.format(self.destinationFloor))
            return
        if (self.destinationFloor in range(1, 19)):
            self.currentFloor = self.destinationFloor
            print('You will go to floor #' + str(self.currentFloor))
        else:
            print('No specified floor, lift stays in place')

#let user input manually
print('How many people are entering?')
enterPeople = int(input())
print('What floor is the lift currently in?')
currentFloor = int(input())
print('What floor are you going to?')
destinationFloor = int(input())
print('How many people are currently in the lift?')
currentPeople = int(input())

#run the whole process
PrelimCheck = Lift(enterPeople, currentFloor, destinationFloor)
PrelimCheck.openDoor(currentPeople)