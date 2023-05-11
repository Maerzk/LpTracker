from xlrd import *
from xlwt import Workbook
from xlutils.copy import copy

wb = Workbook()

def createexcelfile(filename):
    Sheet1 = wb.add_sheet("Sheet1")
    Sheet1.write(0, 0, "Tier")
    Sheet1.write(0, 1, "Rank")
    Sheet1.write(0, 2, "LP")
    Sheet1.write(0, 3, "Points")
    Sheet1.write(0, 4, "Point Difference")
    Sheet1.write(0, 5, "Match ID")
    wb.save(filename + ".xls")

def updateexcelfile(filename, soloDuoData, soloDuoPoints, soloDuoPointsDifference, matchId):
    workbook = open_workbook(filename + ".xls", formatting_info=True)
    worksheet = workbook.sheet_by_name("Sheet1")

    newRowIn = worksheet.nrows
    print(newRowIn)

    writeablecopy = copy(workbook)

    writeablecopy.get_sheet(0).write(newRowIn, 0, soloDuoData["tier"])
    writeablecopy.get_sheet(0).write(newRowIn, 1, soloDuoData["rank"])
    writeablecopy.get_sheet(0).write(newRowIn, 2, soloDuoData["leaguePoints"])
    writeablecopy.get_sheet(0).write(newRowIn, 3, soloDuoPoints)
    writeablecopy.get_sheet(0).write(newRowIn, 4, soloDuoPointsDifference)
    writeablecopy.get_sheet(0).write(newRowIn, 5, matchId)
    writeablecopy.save(filename + ".xls")