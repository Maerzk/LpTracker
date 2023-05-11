import os.path
from apiIntecration import *
from apiDataInterpretation import *
from rankCalculations import *
from exportToSQLite import *

def main(my_ign, my_region, apiKey):

    #creates path to database relative to this file
    databasePathNotNormalized = os.path.join(os.path.dirname(__file__), '../Database/' + my_ign + "Data.db")
    databasePath = os.path.normpath(databasePathNotNormalized)

    #gets dictionarys from riot api
    summonerData = getsummonersdata(my_region, my_ign, apiKey)                          #contains "id", "accountId", "puuid", "name", "profileIconId", "revisionDate", "summonerLevel"

    if "status" in summonerData:                                                                                        #aborts program when
        print(summonerData["status"].get("message") + " - Error " + str(summonerData["status"].get("status_code")))     #summonerData contains
        return                                                                                                          #error status

    leaguev4Data = getv4entriesdata(my_region, summonerData["id"], apiKey)              #contains "leagueId", "summonerId", "summonerName", "queueType", "tier", "rank", "leaguePoints", "wins", "losses", "hotStreak", "veteran", "freshBlood", "inactive", "miniSeries"

    if not leaguev4Data:                                                                #abort program when
        print("no ranked data")                                                         #there is no
        return                                                                          #ranked data

    matchv5Data_matchIds = getmatchv5data_matchids(summonerData["puuid"], 0, 20, apiKey)    #contains game Ids of the last x games 

    if not matchv5Data_matchIds:                                                        #abort program when
        print("no match history found")                                                 #there is no match
        return                                                                          #history after v5 start

    for i in matchv5Data_matchIds:                                                      #checks beginning with
        if "status" in getmatchv5data_gameinfo(i, apiKey):                              #the first matchId
            print(f"{my_ign}\tcustom skipped")
            return                                                                      #wether game info
        else:                                                                           #of that game exists
            latestGameMatchId = i                                                       #and saves the first
            break                                                                       #match Id with existing info

    latestGameData = getmatchv5data_gameinfo(latestGameMatchId, apiKey)                 #contains e.g. "queueId" - 420 is solo - 440 is flex

    if "status" in latestGameData:                                                                                                                              #abort program when
        print(latestGameData)                                                                                                                                   #there is no
        print(latestGameData["status"].get("message") + " - Error " + str(latestGameData["status"].get("status_code")) + " - propably only customs found")      #data for that game
        return                                                                                                                                                  #e.g. when custom

    #var to safe queueid of latest game
    latestGameQueueId = latestGameData["info"]["queueId"]

    #splits leaguev4data into two dictionaries
    try:
        soloDuoData = getsoloduodata(leaguev4Data)
        flexData = getflexdata(leaguev4Data)
    except:
        print("couldn't get data")
        return

    #adds all lp together to get a new value for easier calculations
    soloDuoPoints = calculatepoints(soloDuoData)
    flexPoints = calculatepoints(flexData)

    #checks if there already is a db with that name
    if os.path.isfile(databasePath) == False:
        createtable(databasePath)
        updatetablesolo(databasePath, soloDuoData, soloDuoPoints, 0, 0)
        updatetableflex(databasePath, flexData, flexPoints, 0, 0)
        print("created new database " + my_ign + "Data.db")

    elif os.path.isfile(databasePath) == True:

        #newgameexists returns true if the latest matchid does not match the last matchId in the .db file
        if newgameexists(latestGameMatchId, databasePath, "solo") == True and latestGameQueueId == 420:
            soloDuoPointsDifference = calculatepointsdifference(soloDuoPoints, databasePath, "solo")
            updatetablesolo(databasePath, soloDuoData, soloDuoPoints, soloDuoPointsDifference, latestGameMatchId)
            print(my_ign + "\tnew game exists\tsolo duo")

        elif newgameexists(latestGameMatchId, databasePath, "flex") == True and latestGameQueueId == 440:
            flexPointsDifference = calculatepointsdifference(flexPoints, databasePath, "flex")
            updatetableflex(databasePath, flexData, flexPoints, flexPointsDifference , latestGameMatchId)
            print(my_ign + "\tnew game exists\tflex")

        else:
            print(my_ign + "\tno new ranked games")

    else:
        print("unknown error")

if __name__ == "__main__":
    main()