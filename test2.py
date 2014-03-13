from dinnerTable import *
from itertools import *
from collections import defaultdict


def generateValidTables():
    validTables = []
    genders = ["m", "f", "r", "q", "s"]
    sashes = ["purple", "orange", "scarlet", "black", "blue"]
    emblems = ["star", "planet", "spaceship", "mountain", "ocean"]
    flowers = ["rose", "orchid", "tulip", "carnation", "lily"]
    drinks = ["coffee", "herbal tea", "black tea", "green tea", "water"]

    baseSetPerms = list(permutations([0, 1, 2, 3, 4]))

    #tableM = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    for gIndex in range(len(baseSetPerms)): # gender
        for sIndex in range(len(baseSetPerms)): # sash
            for eIndex in range(len(baseSetPerms)): # emblem
                for fIndex in range(len(baseSetPerms)): # flower
                    for dIndex in range(len(baseSetPerms)): # drink
                        table = []
                        for col in range(5):
                            #tableM[0][col] = genders[baseSetPerms[gIndex][col]] # location at table = individual i's gender
                            #tableM[1][col] = sashes[baseSetPerms[sIndex][col]] # location at table = individual i's sash color
                            #tableM[2][col] = emblems[baseSetPerms[eIndex][col]]
                            #tableM[3][col] = flowers[baseSetPerms[fIndex][col]]
                            #tableM[4][col] = drinks[baseSetPerms[dIndex][col]]
                            table.append(Individual(genders[baseSetPerms[gIndex][col]], sashes[baseSetPerms[sIndex][col]], emblems[baseSetPerms[eIndex][col]], flowers[baseSetPerms[fIndex][col]], drinks[baseSetPerms[dIndex][col]]))
                        dt = dinnerTable(table)
                        dt.checkConditions(False)
                        if dt.errors < 1:
                            validTables.append(dt)
                            print "found one!"
            print "running"

    for each_table in validTables:
        each_table.toString()



generateValidTables()