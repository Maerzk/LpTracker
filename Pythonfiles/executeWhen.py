import time
from main import main
from _keys import DEV_API_KEY, REAL_API_KEY

nameList = ["TheRatak", "Kolosalos", "stizzell", "3429823988349023"]
my_region = "euw1"
developmentApiKey = DEV_API_KEY
realApiKey = REAL_API_KEY

for i in range(len(nameList)):
    main(nameList[i], my_region, realApiKey)
    time.sleep(1)