
class Individual:
    def __init__(self, gender, sash, emblem, flower, drink):
        # if sash == "black":
        #     self.emblem = "planet"
        #
        # if sash == "orange":
        #     self.drink = "coffee"
        #     #the sash to the right has to be scarlet

        self.gender = gender
        self.sash = sash
        self.emblem = emblem
        self.flower = flower
        self.drink = drink
        self.attributes = [self.gender, self.sash, self.emblem, self.flower, self.drink]
        self.ID = 0
        self.setID()

    def toString(self):
        printString = "| "
        for attr in self.attributes:
            printString += str(attr) + " | "
        print printString

    def setID(self):
        if self.gender == "q":
            self.ID = "Quick"
        elif self.gender == "s":
            self.ID = "Sessile"
        elif self.gender == "m":
            self.ID = "Male"
        elif self.gender == "f":
            self.ID = "Female"
        elif self.gender == "r":
            self.ID = "Rachial"

    def isSame(self, anotherIndv):
        if (self.gender == anotherIndv.gender) and (self.sash == anotherIndv.sash) and (self.emblem == anotherIndv.emblem) and (self.flower == anotherIndv.flower) and (self.drink == anotherIndv.drink):
            return True
        else:
            return False