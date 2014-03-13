from individual  import *
class dinnerTable:
    def __init__(self, arrangement):
        self.arrangement = arrangement
        self.genders = ["m", "f", "r", "q", "s"] # where 1 is leftmost, 3 is middle, and 5 is rightmost
        self.sashes = ["purple", "orange", "scarlet", "black", "blue"]
        self.emblems = ["star", "planet", "spaceship", "mountain", "ocean"]
        self.flowers = ["rose", "orchid", "tulip", "carnation", "lily"]
        self.drinks = ["coffee", "herbal tea", "black tea", "green tea", "water"]
        self.allCategories = [self.genders, self.sashes, self.emblems, self.flowers, self.drinks]


        self.errors = []


    def checkConditions(self, askPrint = False):
        ######### CONFIRM UNIQUENESS ##############
        allAttributes = []
        dinnerTableAttributes = []
        emsg = ""


        for category in range(len(self.allCategories)):
            for type in self.allCategories[category]:
                allAttributes.append(type)

        for individual in range(len(self.arrangement)):
            for attr in self.arrangement[individual].attributes:
                dinnerTableAttributes.append(attr)

        #print "All attributes: " + str(allAttributes)
        #print "Dinner Table Attributes: " + str(dinnerTableAttributes)

        for attribute in allAttributes:
            if attribute not in dinnerTableAttributes:
                emsg =  "Your dinner table arrangement does not contain the attribute: '" + str(attribute) + "'"
                self.errors.append(emsg)




        ######### CHECK ALL CONSTRAINTS ###########
        index = 0
        #11 Black tea is served to the person in the middle (arrangement[2])

        if (self.arrangement[2].drink != "black tea"):
            emsg= "The person in the middle is not drinking Black Tea"
            self.errors.append(emsg)

        #12 Quick is at the rightmost seat
        if (self.arrangement[4].gender != "q"):
            emsg= "Quick is not the rightmost person"
            self.errors.append(emsg)

        for p in self.arrangement:
            #3. if female, sash must be purple
            if (p.gender == "f") and (p.sash != "purple"):
                emsg=  "The females' sash must be Purple"
                self.errors.append(emsg)

            #5. if person has an orchid, then someone on their right has to have a rose
            if p.flower == "orchid":
                isRose = False
                for j in self.arrangement:
                    if j.flower == "rose":
                        isRose = True
                if isRose == False:
                    emsg ="There is no person with a Rose to the right of the person with the Orchid"
                    self.errors.append(emsg)

            #6. if the persons sash is orange, their drink has to be coffee.
            if (p.sash == "orange") and (p.drink != "coffee"):
                emsg= "The person with the Orange Sash must drink Coffee (" + str(p.ID) + ")."
                self.errors.append(emsg)

            #7.  if the Male doesnt have herbal tea, return false
            if (p.gender == "m") and (p.drink != "herbal tea"):
                emsg= "The male's drink must be Herbal Tea"
                self.errors.append(emsg)

            #8. if the person with the orange sash is not to the left of the person with the scarlet sash, return false
            if (self.arrangement[index].sash =="orange") and (index!=len(self.arrangement)-1 and self.arrangement[index +1].sash != "scarlet"):
                emsg =  "The person with the Orange Sash must be to the left of the person with the Scarlet Sash"
                self.errors.append(emsg)

            #9 The person with the star emblem must also have a tulip as their flower.
            if (p.emblem == "star") and (p.flower != "tulip"):
                emsg= "This persons emblem is the Star Emblem. Their flower must be a Tulip (" + str(p.ID) + ")."
                self.errors.append(emsg)

            #10 If their sash is black, they must also have the planet emblem
            if (p.sash == "black") and (p.emblem != "planet"):
                emsg= "This persons sash is black. They must also have the Planet Emblem (" + str(p.ID) + ")."
                self.errors.append(emsg)

            #13 If the spaceship emblem is not adjacent to the carnation flower, return false
            #Note: the symbol '^' represents XOR (exclusive OR)
            if (p.flower =="carnation") and not (
                        (index !=0 and self.arrangement[index- 1].emblem == "spaceship") ^ (index!=len(self.arrangement)-1 and self.arrangement[index + 1].emblem == "spaceship")):
                emsg= "The Spaceship Emblem is not adjacent to the Carnation flower"
                self.errors.append(emsg)

            #14 The planet emblem is adjacent to the place with the lily
            #Note: the symbol '^' represents XOR (exclusive OR)
            if (p.flower == "lily") and not (
                        (index !=0 and self.arrangement[index - 1].emblem == "planet") ^ (index!=len(self.arrangement)-1 and self.arrangement[index + 1].emblem == "planet")):
                emsg= "The Planet Emblem is not adjacent to the Lily"
                self.errors.append(emsg)

            #16 Green tea is served to the person with the mountain emblem
            if (p.drink == "green tea") and (p.emblem != "mountain"):
                emsg = "The person drinking Green Tea must also have the Mountain Emblem (" + str(p.ID) + ")."
                self.errors.append(emsg)


            index += 1  # increment index at the end of the evaluation

        if (askPrint):
            if len(self.errors) < 1:
                return "Your dinner table is acceptable."
            else:
                for msg in self.errors:
                    print "*" + str(msg)

    def toString(self):
        print "Table (Leftmost):"
        for person in self.arrangement:
            person.toString()





