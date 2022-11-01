from csv import writer
import requests
import json
from datetime import date
import matplotlib.pyplot as plt
import sqlite3
from os import path

#today = date.today()
#start_date = ('start_date=' + str(today))
#end_date = ('end_date=' + str(today))
myList = []

def listcreate():
    file1 = json.loads(open('myData.json').read())

    for x in file1["daily"]["temperature_2m_max"]:
        myList.append(x)

    for x in file1["daily"]["temperature_2m_min"]:
        myList.append(x)

    for x in file1["daily"]["sunrise"]:
        myList.append(x)

    for x in file1["daily"]["sunset"]:
        myList.append(x)

def temphigh():
    file1 = json.loads(open('myData.json').read())

    for x in file1["daily"]["temperature_2m_max"]:
        print(str(x) + "°F")
        main()

def templow():
    file1 = json.loads(open('myData.json').read())

    for x in file1["daily"]["temperature_2m_min"]:
        print(str(x) + "°F")
        main()

def sunrise():
    file1 = json.loads(open('myData.json').read())

    for x in file1["daily"]["sunrise"]:
        print(x)
        main()

def sunset():
    file1 = json.loads(open('myData.json').read())

    for x in file1["daily"]["sunset"]:
        print(x)
        main()

#def notifications():
    #file1 = json.loads(open('myData.json').read())

    #for x in file1["daily"]["temperature_2m_min"]:
        #if x <= 38:
            #print("Don't forget your Jacket today!")

    #for x in file1["daily"]["temperature_2m_max"]:
        #if x >= 85:
            #print("Wear shorts! Its hot!")

def sql():
    conn = sqlite3.connect("/Users/willballentine/Documents/datasort/weather.db")
    c = conn.cursor()
    listcreate()
    c.execute('Insert into dailyweather values (?,?,?,?)', myList)
    conn.commit()
    conn.close()
    print(c.rowcount)

def main():

    with open('myData.json', 'w') as f:
        count = 0
        url = ("https://api.open-meteo.com/v1/forecast?latitude=38.2527&longitude=85.7585&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York&start_date=2022-06-08&end_date=2022-10-31")
        response = requests.request("GET", url)
        today = str(response.json())
        today2 = today.replace("\'", "\"")
        

        f.write(today2)


        count = count + 1
    #print(count)
    f.close()
   # notifications()
    sql()
    print("1. High Temp \n 2. Low Temp \n 3. Sunrise \n 4. Sunset \n 5. Quit")
    userinput = input("What weather data would you like?   ")

    if userinput == "1":
        temphigh()
    elif userinput == "2":
        templow()
    elif userinput == "3":
        sunrise()
    elif userinput == "4":
        sunset()
    elif userinput == "5":
        exit()
    elif print('not an option, try again'):
        main()


main()