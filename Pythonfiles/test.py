import os.path
import sys
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

try:
    matchIds = getmatchv5data_matchids(summonerData["puuid"], 0, 101, apiKey)
except:
    matchIds = []

print(matchIds)