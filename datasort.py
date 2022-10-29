import csv
import requests
import json

def temphigh():
    file1 = json.loads(open('myData.json').read())

    for x in file1["daily"]["temperature_2m_max"]:
        print(x)
        main()

def templow():
    file1 = json.loads(open('myData.json').read())

    for x in file1["daily"]["temperature_2m_min"]:
        print(x)
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

def main():

    with open('myData.json', 'w') as f:
        count = 0
        url = "https://api.open-meteo.com/v1/forecast?latitude=38.2527&longitude=85.7585&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York&start_date=2022-10-29&end_date=2022-10-29"
        response = requests.request("GET", url)
        today = str(response.json())
        today2 = today.replace("\'", "\"")
        

        f.write(today2)


        count = count + 1
    #print(count)
    f.close()
    print("1. High Temp \n 2. Low Temp \n 3. sunrise \n 4. sunset")
    userinput = input("What weather data would you like?")

    if userinput == "1":
        temphigh()
    elif userinput == "2":
        templow()
    elif userinput == "3":
        sunrise()
    elif userinput == "4":
        sunset()
    elif print('not an option, try again'):
        main()


main()