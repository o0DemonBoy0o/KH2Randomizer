import random
from enum import Enum
from List.configDict import locationType, locationCategory
from dataclasses import dataclass

@dataclass (frozen=True)
class KH2Objective:
    Name: str
    Location: locationType
    LocationId: int
    Category: locationCategory
    Difficulty: int = 0
    Boss: bool = False

STT_Objectives = [
    KH2Objective("Defeat Twilight Thorn",                           locationType.STT, 33,     locationCategory.ITEMBONUS, True),
    KH2Objective("Defeat Axel I",                                   locationType.STT, 73,     locationCategory.ITEMBONUS),
    KH2Objective("Fight Setzer",                                    locationType.STT, 389,    locationCategory.POPUP),
    KH2Objective("Defeat Axel II",                                  locationType.STT, 34,     locationCategory.STATBONUS, True),
]

TT_Objectives = [
	KH2Objective("Talk to the 3 Fairies",                           locationType.TT,  286,    locationCategory.POPUP),
    KH2Objective("Defeat the Sandlot Berserkers",                   locationType.TT,  294,    locationCategory.POPUP,1),
    KH2Objective("Fight alongside Axel",                            locationType.TT,  63,     locationCategory.ITEMBONUS,2),
]

HB_Objectives = [
    KH2Objective("Defend the Bailey Gate",                          locationType.HB,  47,     locationCategory.ITEMBONUS),
    KH2Objective("Defeat Demyx",                                    locationType.HB,  28,     locationCategory.HYBRIDBONUS,1, True),
    KH2Objective("Defeat the 1000 Heartless",                       locationType.HB,  60,     locationCategory.ITEMBONUS,2),
]

CoR_Objectives = [
    KH2Objective("Reach the end of the Cavern of Rememberance",     locationType.CoR, 579,    locationCategory.CHEST,2),
]

TTR_Objectives = [
    KH2Objective("Reach the end of the Transport to Rememberance", locationType.TTR, 72,      locationCategory.STATBONUS,3),
]

LoD_Objectives = [
    KH2Objective("Climb the Mountain Trail",                        locationType.LoD, 495,    locationCategory.POPUP,0, True),
    KH2Objective("Fight the Enemies in the Village Cave",           locationType.LoD, 43,     locationCategory.ITEMBONUS,0, True),
    KH2Objective("Defeat Shan-Yu",                                  locationType.LoD, 9,      locationCategory.HYBRIDBONUS,1, True),
    KH2Objective("Defeat Storm Rider",                              locationType.LoD, 10,     locationCategory.ITEMBONUS,2, True),
]

BC_Objectives = [
    KH2Objective("Defeat Thresholder",                              locationType.BC,  2,      locationCategory.ITEMBONUS, True),
    KH2Objective("Help Beast come to his senses",                   locationType.BC,  12,     locationCategory.STATBONUS),
    KH2Objective("Defeat Dark Thorn",                               locationType.BC,  3,      locationCategory.HYBRIDBONUS, True),
    KH2Objective("Defeat Xaldin",                                   locationType.BC,  4,    locationCategory.HYBRIDBONUS,2, True),
]

DC_Objectives = [
    KH2Objective("Escort the Queen",                                locationType.DC,  38,     locationCategory.HYBRIDBONUS),
    KH2Objective("Fight through the Windows of Time",               locationType.DC,  368,    locationCategory.POPUP,1),
    KH2Objective("Stop Pete from escaping the Waterway",            locationType.DC,  16,     locationCategory.ITEMBONUS,1),
    KH2Objective("Defeat Pete at the Warf",                         locationType.DC,  17,     locationCategory.HYBRIDBONUS,2, True),
]

PR_Objectives = [
    KH2Objective("Stall for time on Isle de Murta",                 locationType.PR,  329,    locationCategory.POPUP),
    KH2Objective("Defend the Interceptor from the Pirates",         locationType.PR,  62,     locationCategory.ITEMBONUS),
    KH2Objective("Stop the Explosive Barrels",                      locationType.PR,  39,     locationCategory.STATBONUS),
    KH2Objective("Defeat Barbossa",                                 locationType.PR,  21,    locationCategory.HYBRIDBONUS,1, True),
    KH2Objective("Defeat Grim Reaper I",                            locationType.PR,  59,     locationCategory.ITEMBONUS,1, True),
    #KH2Objective("Find all the missing medallions", locationType.PR, 999),
    KH2Objective("Defeat Grim Reaper II",                           locationType.PR,  22,    locationCategory.ITEMBONUS,2, True),
]

AG_Objectives = [
    KH2Objective("Escort Abu",                                      locationType.Agrabah, 42, locationCategory.ITEMBONUS),
    KH2Objective("Survive the Treasure Room ambush",                locationType.Agrabah, 46, locationCategory.STATBONUS,1),
    KH2Objective("Defeat the Elemental Lords",                      locationType.Agrabah, 37, locationCategory.ITEMBONUS,1, True),
    KH2Objective("Defeat Jafar",                                    locationType.Agrabah, 15, locationCategory.ITEMBONUS,2, True),
]

HT_Objectives = [
    KH2Objective("Defeat Prison Keeper",                            locationType.HT, 18,      locationCategory.HYBRIDBONUS, True),
    KH2Objective("Defeat Oogie Boogie",                             locationType.HT, 19,      locationCategory.STATBONUS,1, True),
    KH2Objective("Capture the kids",                                locationType.HT, 40,      locationCategory.STATBONUS,1),
    KH2Objective("Find the stolen presents",                        locationType.HT, 297,     locationCategory.POPUP,1),
    KH2Objective("Create the decoy presents",                       locationType.HT, 298,    locationCategory.POPUP,1),
    KH2Objective("Defeat The Experiment",                           locationType.HT, 20,      locationCategory.STATBONUS,2, True),
]

PL_Objectives = [
    KH2Objective("Reunite with Simba",                              locationType.PL, 264,     locationCategory.POPUP),
    KH2Objective("Rescue Timon and Pumbaa",                         locationType.PL, 49,      locationCategory.STATBONUS),
    KH2Objective("Defeat Scar",                                     locationType.PL, 29,      locationCategory.STATBONUS,1, True),
    KH2Objective("Get info about Scar out of the Hyenas",           locationType.PL, 50,      locationCategory.STATBONUS,1),
    KH2Objective("Defeat Groundshaker",                             locationType.PL, 30,      locationCategory.HYBRIDBONUS,2, True),
]

SP_Objectives = [
    KH2Objective("Survive the Dataspace Attack",                    locationType.SP, 45,      locationCategory.STATBONUS),
    KH2Objective("Defeat Hostile Program",                          locationType.SP, 31,      locationCategory.HYBRIDBONUS,1, True),
    KH2Objective("Ride the Solar Sailer",                           locationType.SP, 61,      locationCategory.ITEMBONUS,1),
    KH2Objective("Defeat MCP",                                      locationType.SP, 32,      locationCategory.HYBRIDBONUS,2, True),
]

TWTNW_Objectives = [
    KH2Objective("Defeat Roxas",                                    locationType.TWTNW, 69,   locationCategory.HYBRIDBONUS, True),
    KH2Objective("Defeat Xigbar",                                   locationType.TWTNW, 23,   locationCategory.STATBONUS,1, True),
    KH2Objective("Defeat Luxord",                                   locationType.TWTNW, 24,   locationCategory.HYBRIDBONUS,1, True),
    KH2Objective("Defeat Saix",                                     locationType.TWTNW, 25,   locationCategory.STATBONUS,1, True),
    #KH2Objective("Reunite with Riku",                               locationType.TWTNW, 535,  ),
    KH2Objective("Defeat Xemnas",                                   locationType.TWTNW, 26,   locationCategory.DOUBLEBONUS,2, True),
]

OC_Objectives = [
    KH2Objective("Defeat Cerberus",                                 locationType.OC, 5,       locationCategory.ITEMBONUS, True),
    KH2Objective("Complete Phil's Training",                        locationType.OC, 57,      locationCategory.ITEMBONUS),
    KH2Objective("Defeat Pete at The Lock",                         locationType.OC, 6,       locationCategory.ITEMBONUS,1),
    KH2Objective("Defeat Hydra",                                    locationType.OC, 7,       locationCategory.HYBRIDBONUS,1, True),
    KH2Objective("Defeat the ambush in Hades' Chamber",             locationType.OC, 295,     locationCategory.POPUP,1),
    KH2Objective("Defeat Hades",                                    locationType.OC, 8,       locationCategory.HYBRIDBONUS,2, True),
]

HAW_Objectives = [
    KH2Objective("Explore the Spooky Cave",                         locationType.HUNDREDAW, 485, locationCategory.POPUP,2),
    KH2Objective("Help Pooh out of the jar of hunny",               locationType.HUNDREDAW, 539, locationCategory.POPUP,3),
]

AT_Objectives = [
    KH2Objective("Participate in the Musical",                      locationType.Atlantica, 367, locationCategory.POPUP),
    KH2Objective("Defeat Ursula",                                   locationType.Atlantica, 287, locationCategory.POPUP,2),
    KH2Objective("Celebrate with everyone under the sea",           locationType.Atlantica, 538, locationCategory.POPUP,3),
]

Cups_Objectives = [
    KH2Objective("Win the pain & Panic Cup",    locationType.OCCups, 540, locationCategory.POPUP),
    KH2Objective("Win the Cerberus Cup",        locationType.OCCups, 542, locationCategory.POPUP,1),
    KH2Objective("Win the Titan Cup",           locationType.OCCups, 541, locationCategory.POPUP,1),
    KH2Objective("Win the Goddess of Fate Cup", locationType.OCCups, 517, locationCategory.POPUP,2)
]

#Paradox_Objectives = [KH2Objective("Win the Hades Paradox Cup", locationType.OCParadoxCup, 518, locationCategory.POPUP)]

Form_Objectives = [
    KH2Objective("Reach Valor Form Level 3",    locationType.FormLevel, 3,   locationCategory.VALORLEVEL,   0),
    KH2Objective("Reach Wisdom Form Level 3",   locationType.FormLevel, 3,   locationCategory.WISDOMLEVEL,  0),
    KH2Objective("Reach Limit Form Level 3",    locationType.FormLevel, 3,   locationCategory.LIMITLEVEL,   0),
    KH2Objective("Reach Master Form Level 3",   locationType.FormLevel, 3,   locationCategory.MASTERLEVEL,  0),
    KH2Objective("Reach Final Form Level 3",    locationType.FormLevel, 3,   locationCategory.FINALLEVEL,   0),

    KH2Objective("Reach Valor Form Level 5",    locationType.FormLevel, 5,    locationCategory.VALORLEVEL,  1),
    KH2Objective("Reach Wisdom Form Level 5",   locationType.FormLevel, 5,   locationCategory.WISDOMLEVEL,  1),
    KH2Objective("Reach Limit Form Level 5",    locationType.FormLevel, 5,   locationCategory.LIMITLEVEL,   1),
    KH2Objective("Reach Master Form Level 5",   locationType.FormLevel, 5,   locationCategory.MASTERLEVEL,  1),
    KH2Objective("Reach Final Form Level 5",    locationType.FormLevel, 5,   locationCategory.FINALLEVEL,   1),

    KH2Objective("Reach Valor Form Level 7",    locationType.FormLevel, 7,    locationCategory.VALORLEVEL,  2),
    KH2Objective("Reach Wisdom Form Level 7",   locationType.FormLevel, 7,   locationCategory.WISDOMLEVEL,  2),
    KH2Objective("Reach Limit Form Level 7",    locationType.FormLevel, 7,   locationCategory.LIMITLEVEL,   2),
    KH2Objective("Reach Master Form Level 7",   locationType.FormLevel, 7,   locationCategory.MASTERLEVEL,  2),
    KH2Objective("Reach Final Form Level 7",    locationType.FormLevel, 7,   locationCategory.FINALLEVEL,   2)    
]

#Sephi_objectives = [KH2Objective("Defeat Sephiroth", locationType.Sephi, 35, locationCategory.STATBONUS)]

#LW_Objectives = [KH2Objective("Defeat Terra", locationType.LW, 70, locationCategory.STATBONUS)]

Puzz_Objectives = [
KH2Objective("Complete the Awakening Puzzle", 	locationType.Puzzle, 0, locationCategory.CREATION, 1),
KH2Objective("Complete the Heart Puzzle", 		locationType.Puzzle, 1, locationCategory.CREATION, 1),
KH2Objective("Complete the Duality Puzzle", 	locationType.Puzzle, 2, locationCategory.CREATION, 2),
KH2Objective("Complete the Frontier Puzzle", 	locationType.Puzzle, 3, locationCategory.CREATION, 2),
KH2Objective("Complete the Daylight Puzzle", 	locationType.Puzzle, 4, locationCategory.CREATION, 3),
KH2Objective("Complete the Sunset Puzzle", 		locationType.Puzzle, 5, locationCategory.CREATION, 3)    
]

#Other_Objectives = [
#    KH2Objective("Reach Level 50", locationType.Level, 34),
#    KH2Objective("Rescue Piglet", locationType.HUNDREDAW, 34),
#    KH2Objective("Help Rabbit gather hunny", locationType.HUNDREDAW, 34),
#    KH2Objective("Bounce with Tigger and Roo", locationType.HUNDREDAW, 34),
#]


def generateObjectives(enabledLocations, datasplit = False, difficulty = 'OBJECTIVES'):
    fullList = []
    datas = False
    absent = False

    if locationType.DataOrg in enabledLocations:
        datas = True
    if locationType.AS in enabledLocations:
        absent = True

    if locationType.LoD in enabledLocations:
        fullList.extend(LoD_Objectives)
        if datas:
            fullList.extend([KH2Objective("Defeat Xigbar (Data)", locationType.DataOrg, 555, locationCategory.POPUP,3, True)])

    if locationType.BC in enabledLocations:
        fullList.extend(BC_Objectives)
        if datas:
            fullList.extend([KH2Objective("Defeat Xaldin (Data)", locationType.DataOrg, 559, locationCategory.POPUP,3, True)])

    if locationType.HB in enabledLocations:
        fullList.extend(HB_Objectives)
        if datas:
            fullList.extend([KH2Objective("Defeat Demyx (Data)", locationType.DataOrg, 560, locationCategory.POPUP,3, True)])
        if locationType.Sephi in enabledLocations:
            fullList.extend([KH2Objective("Defeat Sephiroth", locationType.Sephi, 35, locationCategory.STATBONUS,3, True)])

    if locationType.CoR in enabledLocations:
        fullList.extend(CoR_Objectives)

    if locationType.TTR in enabledLocations:
        fullList.extend(TTR_Objectives)

    if locationType.TT in enabledLocations:
        fullList.extend(TT_Objectives)
        if datas:
            fullList.extend([KH2Objective("Defeat Axel (Data)", locationType.DataOrg, 561, locationCategory.POPUP,3, True)])

    if locationType.TWTNW in enabledLocations:
        fullList.extend(TWTNW_Objectives)
        if datas:
            fullList.extend([KH2Objective("Defeat Final Xemnas (Data)", locationType.DataOrg, 554, locationCategory.POPUP,3, True)])

    if locationType.SP in enabledLocations:
        fullList.extend(SP_Objectives)
        if absent:
            fullList.extend([KH2Objective("Defeat Larxene (AS)", locationType.AS, 68, locationCategory.STATBONUS,2, True)])
        if datas and datasplit:
            fullList.extend([KH2Objective("Defeat Larxene (Data)", locationType.DataOrg, 552, locationCategory.POPUP,3, True)])


    if locationType.Atlantica in enabledLocations:
        fullList.extend(AT_Objectives)

    if locationType.PR in enabledLocations:
        fullList.extend(PR_Objectives)
        if datas:
            fullList.extend([KH2Objective("Defeat Luxord (Data)", locationType.DataOrg, 557, locationCategory.POPUP,3, True)])

    if locationType.OC in enabledLocations:
        fullList.extend(OC_Objectives)
        if absent:
            fullList.extend([KH2Objective("Defeat Zexion (AS)", locationType.AS, 66, locationCategory.STATBONUS,2, True)])
        if datas and datasplit:
            fullList.extend([KH2Objective("Defeat Zexion (Data)", locationType.DataOrg, 551, locationCategory.POPUP,3, True)])
        if locationType.OCCups in enabledLocations:
            fullList.extend(Cups_Objectives)
        if locationType.OCParadoxCup in enabledLocations:
            fullList.extend([KH2Objective("Win the Hades Paradox Cup", locationType.OCParadoxCup, 518, locationCategory.POPUP,3)])

    if locationType.Agrabah in enabledLocations:
        fullList.extend(AG_Objectives)
        if absent:
            fullList.extend([KH2Objective("Defeat Lexaeus (AS)", locationType.AS, 65, locationCategory.STATBONUS, 2, True)])
        if datas and datasplit:
            fullList.extend([KH2Objective("Defeat Lexaeus (Data)", locationType.DataOrg, 550, locationCategory.POPUP, 3, True)])

    if locationType.HT in enabledLocations:
        fullList.extend(HT_Objectives)
        if absent:
            fullList.extend([KH2Objective("Defeat Vexen (AS)", locationType.AS, 64, locationCategory.STATBONUS, 2, True)])
        if datas and datasplit:
            fullList.extend([KH2Objective("Defeat Vexen (Data)", locationType.DataOrg, 549, locationCategory.POPUP, 3, True)])

    if locationType.PL in enabledLocations:
        fullList.extend(PL_Objectives)
        if datas:
            fullList.extend([KH2Objective("Defeat Saix (Data)", locationType.DataOrg, 556, locationCategory.POPUP,3, True)])

    if locationType.DC in enabledLocations:
        fullList.extend(DC_Objectives)
        if absent:
            fullList.extend([KH2Objective("Defeat Marluxia (AS)", locationType.AS, 67, locationCategory.STATBONUS,2, True)])
        if datas and datasplit:
            fullList.extend([KH2Objective("Defeat Marluxia (Data)", locationType.DataOrg, 553, locationCategory.POPUP,3, True)])
        if locationType.LW in enabledLocations:
            fullList.extend([KH2Objective("Defeat Lingering Will", locationType.LW, 70, locationCategory.STATBONUS,3, True)])

    if locationType.HUNDREDAW in enabledLocations:
        fullList.extend(HAW_Objectives)

    if locationType.STT in enabledLocations:
        fullList.extend(STT_Objectives)
        if datas:
            fullList.extend([KH2Objective("Defeat Roxas (Data)", locationType.DataOrg, 558, locationCategory.POPUP,3, True)])

    if locationType.FormLevel in enabledLocations:
        fullList.extend(Form_Objectives)

    if locationType.Puzzle in enabledLocations:
        fullList.extend(Puzz_Objectives)

    #TODO: support for sora level?

    #quick parse to remove everything that isn't a boss for boss only mode
    if difficulty == 'OBJECTIVESBOSS':
        fullList = [task for task in fullList if task.Boss]

    finalList = []
    for x in range(13):
        task = random.choice(fullList)
        taskDiff = task.Difficulty
        decided = decideTask(difficulty, taskDiff)

        while decided == False:
            task = random.choice(fullList)
            taskDiff = task.Difficulty
            decided = decideTask(difficulty, taskDiff)

        finalList.append(task)
        fullList.remove(task)

    return finalList

def decideTask(mode, diff):
    chances = [100, 100, 100, 100]
    useTask = False

    #if mode in ['OBJECTIVES', 'OBJECTIVESBOSS']:
    #    return True
    if mode == 'OBJECTIVESEASY':
        chances = [100, 75, 10, 0]
    if mode == 'OBJECTIVESMID':
        chances = [60, 100, 30, 15]
    if mode == 'OBJECTIVESHARD':
        chances = [25, 50, 70, 40]
    if mode == 'OBJECTIVESVHARD':
        chances = [0, 20, 85, 100]
    
    testInt = random.randint(1, 100)

    if diff == 0:
        if testInt <= chances[0]:
            useTask = True
    elif diff == 1:
        if testInt <= chances[1]:
            useTask = True
    elif diff == 2:
        if testInt <= chances[2]:
            useTask = True
    elif diff == 3:
        if testInt <= chances[3]:
            useTask = True

    return useTask