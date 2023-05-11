import sqlite3
import json

def createtable(databasePath,):
    con = sqlite3.connect(databasePath)
    cur = con.cursor()
    cur.execute('''CREATE TABLE solodata
               (tier text, rank text, lp int, points int, pointdifference int, matchid text)''')
    cur.execute('''CREATE TABLE flexdata
               (tier text, rank text, lp int, points int, pointdifference int, matchid text)''')
    cur.execute('''CREATE TABLE matchhistory
               (matchid text, queueid text, gamecreationtime int, matchinfo json)''')
    con.close()

def createtablematchhistory(databasePath):
    con = sqlite3.connect(databasePath)
    cur = con.cursor()
    cur.execute('''CREATE TABLE matchhistory
               (matchid text, matchqueueid text, gamestarttimestamp int, matchinfo text)''')
    con.close()

def updatetablesolo(databasePath, soloDuoData, soloDuoPoints, soloDuoPointsDifference, matchId):
    con = sqlite3.connect(databasePath)
    cur = con.cursor()
    cur.execute("insert into solodata values (?, ?, ?, ?, ?, ?)", (soloDuoData["tier"], soloDuoData["rank"], int(soloDuoData["leaguePoints"]), soloDuoPoints, soloDuoPointsDifference, matchId))
    con.commit()
    con.close()

def updatetableflex(databasePath, flexData, flexPoints, flexPointsDifference, matchId):
    con = sqlite3.connect(databasePath)
    cur = con.cursor()
    cur.execute("insert into flexdata values (?, ?, ?, ?, ?, ?)", (flexData["tier"], flexData["rank"], int(flexData["leaguePoints"]), flexPoints, flexPointsDifference, matchId))
    con.commit()
    con.close()

def updatetablematchhistory(databasePath, matchId, matchInfo, reducedMatchInfo):
    con = sqlite3.connect(databasePath)
    cur = con.cursor()
    cur.execute("insert into matchhistory values (?, ?, ?, ?)", (matchId, matchInfo["info"]["queueId"], int(matchInfo["info"]["gameCreation"]), json.dumps(reducedMatchInfo)))
    con.commit()
    con.close()

def printdatabase(databasePath):
    con = sqlite3.connect(databasePath)
    cur = con.cursor()
    cur.execute("SELECT * FROM solodata")
    print(cur.fetchall())
    cur.execute("SELECT * FROM flexdata")
    print(cur.fetchall())
    con.close()

def printmatchhistory(databasePath):
    con = sqlite3.connect(databasePath)
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM matchhistory")
    except:
        print("no matchhistory to print")
    print(cur.fetchall())
    con.close()

def deletetable(databasePath, tablename):
    con = sqlite3.connect(databasePath)
    cur = con.cursor()
    cur.execute("DROP TABLE " + tablename)
    con.commit()
    con.close()

