from bs4 import BeautifulSoup
import html.parser
import json
import csv
import time
import re
import requests

h = html.parser

urls = []
with open('Yelp.csv', 'r' ) as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        url = str(line[0]).strip()
        if "https://www.yelp.com" in url:
            urls.append(url)
        else:
            urls.append("https://www.yelp.com"+url)
print(len(urls))

start_pos = int(input("start position: "))
headers = {
    'authority': 'www.yelp.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
}

for i in range(start_pos,len(urls)):
    url = urls[i]
    try:
        while True:
            try:
                r = requests.get(url, headers=headers)
                soup = BeautifulSoup(r.text, 'html.parser')
                time.sleep(1)
                status = str(r.status_code).strip()
                if status=="200":
                    break
                else:
                    continue
            except:
                continue

        print(i,status)
        name,address,website,phone,amenities = [""]*5

        try:
            name    = str(soup.select_one('h1[class="css-11q1g5y"]').text).strip()
        except:
            pass

        try:
            address = str(soup.select_one('address[class]').text).strip()
        except:
            pass

        try:
            encid = str(soup.select_one('[name="yelp-biz-id"]')["content"]).strip()
            data = soup.select_one('script[data-apollo-state]')
            data = h.unescape(str(data.contents[0]).replace("<!--","").replace("-->",""))
            data = json.loads(data)

            amenities = ""
            n=0
            while True:
                try:
                    string = '$ROOT_QUERY.business({"encid":"' + encid + '"}).organizedProperties({"clientPlatform":"WWW"}).0.properties.' + str(n)
                    amenity = str(data[string]["displayText"]).strip()
                    amenities += amenity + ", "
                    n+=1
                except:
                    break
            amenities = amenities.strip(", ")
        except:
            amenities = ""
        try:
            items = soup.select('section[class*="b3__373c0__q1DuY"] [class*="2__373c0__3Zpeq"]')
        except:
            items = []

        for item in items:
            try:
                label  = str(item.select_one('[class="css-aml4xx"]').text).strip()
            except:
                label  = ""

            try:
                result  = str(item.select_one('[class="css-1h1j0y3"]').text).strip()
            except:
                result  = ""

            if label=="Business website":
                website = result
            if label=="Phone number":
                phone = result

        f_data = [url,name,address,phone,website,amenities]
        with open(f'91_output_b.csv', 'a', newline='', encoding="utf-8", errors="ignore") as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerow(f_data)
    except:
        pass
    #time.sleep(2)
