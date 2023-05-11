import requests
import json

def getsummonersdata(my_region, my_ign, apiKey):
    summoners_request = requests.get("https://" + my_region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + my_ign + "?api_key=" + apiKey)
    summoners_dictionary = json.loads(summoners_request.text)
    #print("summoners:")
    #print(summoners_dictionary)
    return summoners_dictionary

def getv4entriesdata(my_region, my_id, apiKey):
    v4entries_request = requests.get("https://" + my_region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + my_id + "?api_key=" + apiKey)
    v4entries_dictionary = json.loads(v4entries_request.text)
    #print("v4entries:")
    #print(v4entries_dictionary)
    return v4entries_dictionary

def getmatchv5data_matchids(my_puuid, startGame, numberOfGames, apiKey):
    matchv5_request = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/" + my_puuid + "/ids?start=" + str(startGame) + "&count=" + str(numberOfGames) + "&api_key=" + apiKey)
    matchv5_dictionary = json.loads(matchv5_request.text)
    #print("matchv5:")
    #print(matchv5_dictionary)
    return matchv5_dictionary

def getmatchv5data_gameinfo(matchId, apiKey):
    matchv5_request = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/" + matchId + "?api_key=" + apiKey)
    matchv5_dictionary = json.loads(matchv5_request.text)
    return matchv5_dictionary