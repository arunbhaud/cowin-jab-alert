import requests
import random
import json
import time
import datetime

from collections import OrderedDict
from playsound import playsound

headers_list = [

    # Firefox 77 Mac

     {

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",

        "Accept-Language": "en-US,en;q=0.5",

        "Referer": "https://www.google.com/",

        "DNT": "1",

        "Connection": "keep-alive",

        "Upgrade-Insecure-Requests": "1"

    },

    # Firefox 77 Windows

    {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",

        "Accept-Language": "en-US,en;q=0.5",

        "Accept-Encoding": "gzip, deflate, br",

        "Referer": "https://www.google.com/",

        "DNT": "1",

        "Connection": "keep-alive",

        "Upgrade-Insecure-Requests": "1"

    },

    # Chrome 83 Mac

    {

        "Connection": "keep-alive",

        "DNT": "1",

        "Upgrade-Insecure-Requests": "1",

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

        "Sec-Fetch-Site": "none",

        "Sec-Fetch-Mode": "navigate",

        "Sec-Fetch-Dest": "document",

        "Referer": "https://www.google.com/",

        "Accept-Encoding": "gzip, deflate, br",

        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"

    },

    # Chrome 83 Windows

    {

        "Connection": "keep-alive",

        "Upgrade-Insecure-Requests": "1",

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

        "Sec-Fetch-Site": "same-origin",

        "Sec-Fetch-Mode": "navigate",

        "Sec-Fetch-User": "?1",

        "Sec-Fetch-Dest": "document",

        "Referer": "https://www.google.com/",

        "Accept-Encoding": "gzip, deflate, br",

        "Accept-Language": "en-US,en;q=0.9"

    },

    # Chrome 90 Windows

    {

        "Connection": "keep-alive",

        "Upgrade-Insecure-Requests": "1",

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

        "Sec-Fetch-Site": "same-origin",

        "Sec-Fetch-Mode": "navigate",

        "Sec-Fetch-User": "?1",

        "Sec-Fetch-Dest": "document",

        "Referer": "https://www.google.com/",

        "Accept-Encoding": "gzip, deflate, br",

        "Accept-Language": "en-US,en;q=0.9"

    }

]
 

today = datetime.date.today()

dt_formatted = today.strftime("%d-%m-%Y")

print("Today's date: {}".format(dt_formatted))

pin = input("Enter pincode: ")

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}'.format(pin, dt_formatted)

print(url)

j = 0
i = 1
while 1 == 1:

    if i%100 == 0:
        j = j+1

    #print("i : {}".format(i))
    #print("j : {}".format(j))

    headers = headers_list[j%5]

    #Create a request session

    r = requests.Session()

    r.headers = headers

    response = r.get(url)

    print("Request #%d\nUser-Agent Sent:%s\n\nResponse:"%(i,headers['User-Agent']))

    if response.status_code == 200:
        print(response.json())
        json_data = json.loads(response.text)
        centers = json_data['centers']

        for item in centers:
            sessions = item['sessions']
            for ss in sessions:
                age_limit = ss['min_age_limit']
                slots_available = ss['available_capacity']
                if age_limit == 18 and slots_available > 0:
                    print(item['name'])
                    print(item['address'])
                    print(ss['vaccine'])
                    playsound('alert.mp3')

    else :
        print(response.status_code)

    print("-------------------")
    i = i+1
    time.sleep(3)
