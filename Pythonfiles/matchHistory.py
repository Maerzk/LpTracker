import os.path
import sys
import time
from apiIntecration import *
from exportToSQLite import *
import sqlite3

my_ign = "Kolosalos"
my_region = "euw1"
filename = my_ign + "Data"
apiKey = "RGAPI-d2ff090a-7602-4f97-a8e0-7cc779da5113"

databasePathNotNormalized = os.path.join(os.path.dirname(__file__), '../database/' + filename + ".db")
databasePath = os.path.normpath(databasePathNotNormalized)

summonerData = getsummonersdata(my_region, my_ign, apiKey)

matchIds = []

i = 0

while i < 20:
    matchIds += getmatchv5data_matchids(summonerData["puuid"], i * 100, 100, apiKey)
    time.sleep(1.5)
    i += 1

matchIds.reverse()
print(matchIds)

counter = 0

for matchId in matchIds:
    matchInfo = getmatchv5data_gameinfo(matchId, apiKey)

    if "status" in matchInfo:
        matchInfo = {"info": {"queueId": "Custom", "gameCreation": 0}}
        reducedMatchInfo = matchInfo
    else:
        reducedMatchInfo = matchInfo
        del reducedMatchInfo["info"]["participants"]

    try:
        updatetablematchhistory(databasePath, matchId, matchInfo, reducedMatchInfo)
    except:
        print("not able to update")

    print("match " + str(counter) + " queueId is " + str(matchInfo["info"]["queueId"]))
    time.sleep(1.5)

    counter += 1