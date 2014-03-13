from dinnerTable import *
from itertools import *
from collections import defaultdict

#indv = Individual(gender, sash, emblem, flower, drink)
# Our first working case - hand calculated
# quick = Individual("q", "black", "planet", "rose", "water")
# male  = Individual("m", "blue", "spaceship", "lily", "herbal tea")
# rachial=Individual("r", "scarlet", "ocean", "carnation", "black tea")
# sessile=Individual("s", "orange", "star", "tulip", "coffee")
# female =Individual("f", "purple", "mountain", "orchid", "green tea")
# myDinnerTable  = [female, sessile, rachial, male, quick]

#Our second working case - hand calculated
quick = Individual("q", "black", "planet", "rose", "water")
male  = Individual("m", "scarlet", "spaceship", "orchid", "herbal tea")
rachial=Individual("r", "orange", "ocean", "carnation", "coffee")
sessile=Individual("s", "blue", "mountain", "lily", "green tea")
female =Individual("f", "purple", "star", "tulip", "black tea")
myDinnerTable  = [rachial, male, female, sessile, quick]

#female.toString()
table = dinnerTable(myDinnerTable)
# print table.checkConditions()
# print ""
# table.toString()

validTables = []



## ITS POSSIBLE THE PROBLEM IS IN THE WAY I FILTER THE RESULTS? (filter after whole list of distinct permutations is generated)
## Or am i not generating all of the permutations?


def generateValidTables():
    genders = ["m", "f", "r", "q", "s"]
    sashes = ["purple", "orange", "scarlet", "black", "blue"]
    emblems = ["star", "planet", "spaceship", "mountain", "ocean"]
    flowers = ["rose", "orchid", "tulip", "carnation", "lily"]
    drinks = ["coffee", "herbal tea", "black tea", "green tea", "water"]

    genderPerms = list(permutations(genders))
    emblemPerms = list(permutations(emblems))
    flowerPerms = list(permutations(flowers))
    sashPerms = list(permutations(sashes))
    drinkPerms = list(permutations(drinks))

    numPerms = len(sashPerms)
    allPerms = [genderPerms, sashPerms, emblemPerms, flowerPerms, drinkPerms]
    allPermsDict = defaultdict(list)

    for i in range(5):
        allts = [] # the order of the values of each permutation
        for j in range(numPerms): # 0-119
            t1, t2, t3, t4, t5 = allPerms[i][j]
            ts = [t1, t2, t3, t4, t5]
            allts.append(ts)

        allPermsDict[i] = allts

    #for i in range(5):
    # I AM ONLY CREATING 120 TABLES. I NEED TO BE MAKING 600 -- Involves changing the way i create tables at pIndex
    for pIndex in range(numPerms):
        table = []
        for i in range(5): #
            igender = allPermsDict[0][pIndex][i]
            isash = allPermsDict[1][pIndex][i]
            iemblem = allPermsDict[2][pIndex][i]
            iflower = allPermsDict[3][pIndex][i]
            idrink = allPermsDict[4][pIndex][i]
            table.append(Individual(igender, isash, iemblem, iflower, idrink))
        table = dinnerTable(table)
        table.checkConditions(False)
        #print pIndex
        print "Errors: " + str(len(table.errors))
        #print table.errors
        #table.toString()
        if len(table.errors) < 1:
            validTables.append(table)
            print "Valid Tables Found: " + str(len(validTables))

generateValidTables()
print len(validTables)





