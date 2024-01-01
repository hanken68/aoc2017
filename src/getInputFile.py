import requests
import sys
import aoc
from datetime import date

vars = aoc.getSettingFromFile()
session = vars["aoc_session"]

day = date.today().day
if len(sys.argv)>1:
    day = int(sys.argv[1])

outFile = "./inputs/x.txt"
url= "https://adventofcode.com/2017/day/{id}/input"

cookieSession = {"session": session}
x=requests.get(url.replace("{id}", str(day)), cookies=cookieSession)

file = open(outFile, "w")
file.write(x.text[:-1])
file.close()