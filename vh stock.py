
#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json
from datetime import datetime

# Complete the function below.

def  openAndClosePrices(firstDate, lastDate, weekDay):
    for i in range(5):
        i += 1
        with urlopen(f"https://jsonmock.hackerrank.com/api/stocks/?page={i}")as response:
            source = response.read()
        data = json.loads(source)
        for j in range(len(data["data"])):

            dt1 = datetime.strptime(data["data"][j]["date"], "%d-%B-%Y")
            x = dt1.strftime("%A")

            dt2 = datetime.strptime(firstDate, "%d-%B-%Y")
            dt3 = datetime.strptime(lastDate, "%d-%B-%Y")

            if dt1 >= dt2 and dt1 <= dt3:
                if x == weekDay:
                    print(data["data"][j]["date"], end=" ")
                    print(data["data"][j]["open"], end=" ")
                    print(data["data"][j]["close"])

try:
    _firstDate = str(input())
except:
    _firstDate = None


try:
    _lastDate = str(input())
except:
    _lastDate = None


try:
    _weekDay = str(input())
except:
    _weekDay = None

openAndClosePrices(_firstDate, _lastDate, _weekDay)

