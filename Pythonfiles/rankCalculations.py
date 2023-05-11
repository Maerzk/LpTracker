import sqlite3
import os

def calculatepoints(Data):

    tier = Data["tier"]
    rank = Data["rank"]

    if tier == "IRON":
        tierPoints = 0
    elif tier == "BRONZE":
        tierPoints = 400
    elif tier == "SILVER":
        tierPoints = 800
    elif tier == "GOLD":
        tierPoints = 1200
    elif tier == "PLATINUM":
        tierPoints = 1600
    elif tier == "DIAMOND":
        tierPoints = 2000
    elif tier == "MASTER":
        tierPoints = 2400
    elif tier == "GRANDMASTER":
        tierPoints = 2400
    elif tier == "CHALLENGER":
        tierPoints = 2400
    else: 
        tierPoints = 0

    if rank == "IV":
        rankPoints = 0
    elif rank == "III":
        rankPoints = 100
    elif rank == "II":
        rankPoints = 200
    elif rank == "I":
        rankPoints = 300
    else:
        rankPoints = 0

    lp = Data["leaguePoints"]

    Points = tierPoints + rankPoints + lp
    return Points

def calculatepointsdifference(currentPoints, databasePath, queueType):
    con = sqlite3.connect(databasePath)
    cur = con.cursor()

    if queueType == "solo":
        cur.execute("SELECT * FROM solodata")

    elif queueType == "flex":
        cur.execute("SELECT * FROM flexdata")

    else:
        print("queue type not found")

    allEntries = cur.fetchall()
    length = len(allEntries) - 1
    lastGamesPoints = allEntries[length][3]

    pointsDifference = currentPoints-lastGamesPoints
    return pointsDifference