import sqlite3

def getsoloduodata(leaguev4Data):
    firstObject = leaguev4Data[0]
    secondObject = leaguev4Data[1]
    if firstObject["queueType"] == "RANKED_SOLO_5x5":
        return firstObject
    else:
        return secondObject

def getflexdata(leaguev4Data):
    firstObject = leaguev4Data[0]
    secondObject = leaguev4Data[1]
    if firstObject["queueType"] == "RANKED_FLEX_SR":
        return firstObject
    else:
        return secondObject

def getlatestgame(matchIds):
    for i in matchIds:
        print(i)

def newgameexists(latestGameMatchId, databasePath, queueType):
    con = sqlite3.connect(databasePath)
    cur = con.cursor()

    if queueType == "solo":
        cur.execute("SELECT * FROM solodata")

    elif queueType == "flex":
        cur.execute("SELECT * FROM flexdata")
    
    allEntries = cur.fetchall()
    length = len(allEntries) - 1
    lastGamesMatchId = allEntries[length][5]

    if latestGameMatchId != lastGamesMatchId:
        return True
    else:
        return False