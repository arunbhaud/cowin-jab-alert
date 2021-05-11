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

for i in range(1,9):

    time.sleep(3)

    #Pick a random browser headers

    if i%100 == 0:
        j = j+1

    print(j)

    headers = headers_list[j%5]

    #Create a request session

    r = requests.Session()

    r.headers = headers

    response = r.get(url)

    print("Request #%d\nUser-Agent Sent:%s\n\nResponse:"%(i,headers['User-Agent']))

    if response.status_code == 200:
        print(response.json())
        json_data = json.loads(response.text)
        if i == 7:
            json_data = json.loads("{\"centers\": [{\"center_id\": 659628, \"name\": \"NMMC ESIS Hosp 4 (COVISHIELD)\", \"address\": \"Sector 5 Sector 9 Vashi Navi Mumbai\", \"state_name\": \"Maharashtra\", \"district_name\": \"Thane\", \"block_name\": \"Navi Mumbai Municipal Corporation\", \"pincode\": 400703, \"lat\": 19, \"long\": 72, \"from\": \"08:00:00\", \"to\": \"20:00:00\", \"fee_type\": \"Free\", \"sessions\": [{\"session_id\": \"d79fb562-b019-4f69-81d2-719c02eee673\", \"date\": \"10-05-2021\", \"available_capacity\": 0, \"min_age_limit\": 45, \"vaccine\": \"COVISHIELD\", \"slots\": [\"08:00AM-11:00AM\", \"11:00AM-02:00PM\", \"02:00PM-05:00PM\", \"05:00PM-08:00PM\"]}]}, {\"center_id\": 648945, \"name\": \"NMMC ESIS Hosp 1 (COVISHIELD)\", \"address\": \"Sector 5 Sector 9 Vashi Navi Mumbai\", \"state_name\": \"Maharashtra\", \"district_name\": \"Thane\", \"block_name\": \"Navi Mumbai Municipal Corporation\", \"pincode\": 400703, \"lat\": 19, \"long\": 72, \"from\": \"08:00:00\", \"to\": \"20:00:00\", \"fee_type\": \"Free\", \"sessions\": [{\"session_id\": \"e87f091a-50cc-4c93-a564-ef7b49b56209\", \"date\": \"10-05-2021\", \"available_capacity\": 0, \"min_age_limit\": 45, \"vaccine\": \"COVISHIELD\", \"slots\": [\"08:00AM-11:00AM\", \"11:00AM-02:00PM\", \"02:00PM-05:00PM\", \"05:00PM-08:00PM\"]}]}, {\"center_id\": 631439, \"name\": \"NMMC GENERAL HOSP (2) VASHI10A\", \"address\": \"St Mary Sec 10A Vashi Navi Mumbai\", \"state_name\": \"Maharashtra\", \"district_name\": \"Thane\", \"block_name\": \"Navi Mumbai Municipal Corporation\", \"pincode\": 400703, \"lat\": 19, \"long\": 72, \"from\": \"00:00:00\", \"to\": \"23:30:00\", \"fee_type\": \"Free\", \"sessions\": [{\"session_id\": \"bc9d8dbd-fed2-4929-885e-85e33e15b3a2\", \"date\": \"10-05-2021\", \"available_capacity\": 0, \"min_age_limit\": 45, \"vaccine\": \"COVAXIN\", \"slots\": [\"12:00AM-05:00AM\", \"05:00AM-10:00AM\", \"10:00AM-03:00PM\", \"03:00PM-11:30PM\"]}]}, {\"center_id\": 650189, \"name\": \"NMMC ESIS Hosp 2 (COVISHIELD)\", \"address\": \"Sector 5 Sector 9 Vashi Navi Mumbai\", \"state_name\": \"Maharashtra\", \"district_name\": \"Thane\", \"block_name\": \"Navi Mumbai Municipal Corporation\", \"pincode\": 400703, \"lat\": 19, \"long\": 72, \"from\": \"08:00:00\", \"to\": \"20:00:00\", \"fee_type\": \"Free\", \"sessions\": [{\"session_id\": \"5a019856-01d3-4dc7-b6c1-3e27f1f8fc50\", \"date\": \"10-05-2021\", \"available_capacity\": 0, \"min_age_limit\": 45, \"vaccine\": \"COVISHIELD\", \"slots\": [\"08:00AM-11:00AM\", \"11:00AM-02:00PM\", \"02:00PM-05:00PM\", \"05:00PM-08:00PM\"]}]}, {\"center_id\": 659613, \"name\": \"NMMC ESIS Hosp 3 (COVISHIELD)\", \"address\": \"Sector 5 Sector 9 Vashi Navi Mumbai\", \"state_name\": \"Maharashtra\", \"district_name\": \"Thane\", \"block_name\": \"Navi Mumbai Municipal Corporation\", \"pincode\": 400703, \"lat\": 19, \"long\": 72, \"from\": \"08:00:00\", \"to\": \"20:00:00\", \"fee_type\": \"Free\", \"sessions\": [{\"session_id\": \"f7c4ae18-953c-44c5-899c-0eef41b8e5b6\", \"date\": \"10-05-2021\", \"available_capacity\": 0, \"min_age_limit\": 45, \"vaccine\": \"COVISHIELD\", \"slots\": [\"08:00AM-11:00AM\", \"11:00AM-02:00PM\", \"02:00PM-05:00PM\", \"05:00PM-08:00PM\"]}]}, {\"center_id\": 695388, \"name\": \"General Hosp Vashi 18-44\", \"address\": \"St Mary Sec 10A Vashi Navi Mumbai\", \"state_name\": \"Maharashtra\", \"district_name\": \"Thane\", \"block_name\": \"Navi Mumbai Municipal Corporation\", \"pincode\": 400703, \"lat\": 19, \"long\": 72, \"from\": \"09:00:00\", \"to\": \"17:00:00\", \"fee_type\": \"Free\", \"sessions\": [{\"session_id\": \"1451f1df-dae6-4805-b3c8-cb7c3ef93e78\", \"date\": \"10-05-2021\", \"available_capacity\": 1, \"min_age_limit\": 18, \"vaccine\": \"COVAXIN\", \"slots\": [\"09:00AM-11:00AM\", \"11:00AM-01:00PM\", \"01:00PM-03:00PM\", \"03:00PM-05:00PM\"]}]}]}")
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