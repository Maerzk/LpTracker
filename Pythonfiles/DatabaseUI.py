import os
import sqlite3
from time import sleep

path = os.path.join(os.path.dirname(__file__), '../database/')
path = os.path.normpath(path)

listOfDatabases = (os.listdir(path))
databasePathNotNormalized = os.path.join(os.path.dirname(__file__), '../database/')
databasePath = os.path.normpath(databasePathNotNormalized)

def printHeader():
    print(":::        :::::::::       ::::::::::: :::::::::      :::      ::::::::  :::    ::: :::::::::: :::::::::  ")
    print(":+:        :+:    :+:          :+:     :+:    :+:   :+: :+:   :+:    :+: :+:   :+:  :+:        :+:    :+: ")
    print("+:+        +:+    +:+          +:+     +:+    +:+  +:+   +:+  +:+        +:+  +:+   +:+        +:+    +:+ ")
    print("+#+        +#++:++#+           +#+     +#++:++#:  +#++:++#++: +#+        +#++:++    +#++:++#   +#++:++#:  ")
    print("+#+        +#+                 +#+     +#+    +#+ +#+     +#+ +#+        +#+  +#+   +#+        +#+    +#+ ")
    print("#+#        #+#                 #+#     #+#    #+# #+#     #+# #+#    #+# #+#   #+#  #+#        #+#    #+# ")
    print("########## ###                 ###     ###    ### ###     ###  ########  ###    ### ########## ###    ### ")

def printPlayerData(filename):
    os.system("cls")
    printHeader()
    print("")
    print(filename)
    print("")
    print("solo\t= prints solo duo data")
    print("flex\t= prints flex data")
    print("return\t= return to main window")
    print("")

    while True:
        queueInput = input("Waiting for input\n")
        print("")

        if queueInput == "solo":
            printTable(filename, "solodata")
        elif queueInput == "flex":
            printTable(filename, "flexdata")
        elif queueInput == "return":
            printStart()

def printTable(filename, tableName):
    con = sqlite3.connect(databasePath + "/" +  filename)
    cur = con.cursor()
    cur.execute("SELECT * FROM " + tableName)
    data = cur.fetchall()
    con.close()

    for i in data:
        print(i[0] + " " + i[1] + " " + str(i[2]) + "\t\t" + str(i[3]) + "\t" + str(i[4]) + "\t" + i[5])

    print("")

def printStart():
    os.system("cls")
    printHeader()
    print("")
    print("existing databases:\n")

    for i in listOfDatabases:
        print(i)

    while True:
        print("")
        nameInput = input("enter player name:\n")

        for i in listOfDatabases:
            if nameInput + "Data.db" == i:
                printPlayerData(i)

printStart()
