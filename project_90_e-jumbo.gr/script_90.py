# coding: utf-8

from bs4 import BeautifulSoup
from sku_scraper import sku_scrape
import html.parser
import json
import csv
import time
import re
import requests

f_data = ["Product Link","TITLE","DESCTRIPTION","SKU (CODE)","SIZES","AVAILABILITY at my City","Images","Price €","Category > Subcategory > Subcategory > Subcategory"]
with open('output_90.csv', 'w', newline='', encoding="utf-8", errors="ignore") as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(f_data)

urls = []
with open('urls_90.csv', 'r' ) as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        url = str(line[0]).strip()
        urls.append(url)
print(len(urls))

for i in range(0,len(urls)):
    url = urls[i]
    # print(url)
    headers = {
        'authority': 'www.e-jumbo.gr',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://www.e-jumbo.gr',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': url,
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    }

    params = (
        ('lang', 'el'),
    )

    while True:
        try:
            r_1 = requests.get(url, headers=headers)
            soup = BeautifulSoup(r_1.text, 'html.parser')
            status_1 = str(r_1.status_code)
            if status_1=="200":
                break
            else:
                continue
        except:
            continue

    try:
        name = str(soup.select_one('h1[itemprop="name"]').text).strip()
    except:
        continue

    try:
        price = str(soup.select_one('[class="current-price"]').text).strip()
    except:
        price = ""

    try:
        sku  = str(soup.select_one('[class="code"]').text).replace("Κωδικός Jumbo:","").strip()
    except:
        sku  = ""

    try:
        category = ""
        cats = soup.select('[class="breadcrumb clearfix"] [class="title"]')
        for cat in cats[:4]:
            category += str(cat.text).strip() + " > "
        category = category.strip(" > ")
    except:
        category = ""

    try:
        images = ""
        images_raw=soup.select('a[class="cloud-zoom"]')
        for img in images_raw:
            images += "https:" + str(img["href"]).strip().split(".jpg?")[0] + ".jpg" + "\n"
        images = images.strip("\n")
        #print(images)
    except:
        images = ""

    try:
        description = ""
        sections = soup.select('[class="tabs-content"] [class*="tab-box"]')
        for sec in sections:
            label = str(sec.select_one('[class="title"]').text).strip()
            if label =="Περιγραφή - Χαρακτηριστικά":
                description = str(sec.select_one('[class="dynamic-content"]').text).strip()
    except:
        description = ""

    f_data = [url,name,description,"","","",images,price,category]

    with open('output_90.csv', 'a', newline='', encoding="utf-8", errors="ignore") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(f_data)

    p_details = soup.select_one('article[class*="product-details"]')
    # print(p_details)
    data_parent_id = str(p_details["data-parent-id"]).strip()
    data_path      = str(p_details["data-path"]).strip()


    versions = soup.select('[class="versions-container"] [class*="x-product-details-version-selector"] li')

    sku_data = {}

    for version in versions:
        size  = str(version.select_one('[class="size"]').text).strip()
        skuId = str(version["data-value"]).strip()
        sku_data[skuId] = size

    if len(versions)==0:

        skuId = str(soup.select_one('[id="search-warehouse-wrapper"]')["data-skuid"]).strip()
        sku_data[skuId] = "None"
        #print(skus)
        #print(skuIds)
        #print(sizes)
        #print()

    for sku_key in sku_data.keys():

        skuId = sku_key
        size  = sku_data[skuId]
        try:
            sku   = sku_scrape(data_parent_id,data_path,skuId)
        except:
            continue

        data = {"skuId":int(skuId),"skuCode":int(sku),"countryCode":"CY","zipCode":"","maxDistance":1000000,"ignoreAvailability":'true',"geoLocationWithZipCode":'true',"topAvailableWarehouse":100000,"hasGeolocation":'false',"latitude":0,"longitude":0}
        data = json.dumps(data)

        while True:
            try:
                r_2 = requests.post('https://www.e-jumbo.gr/services/EcomService.svc/GetProductAvailableWarehouses', headers=headers, params=params, data=data)
                w_data = json.loads(r_2.json()["d"]["data"])
                status_2 = str(r_2.status_code)
                if status_2=="200":
                    break
                else:
                    continue
            except:
                continue

        availability = "Μη διαθέσιμο"

        try:
            warehouses   = w_data["WarehousesGrouped"][0]["Items"]
        except:
            warehouses   =  []
            #availability = str(soup.select_one('[class*="availability-text"]').text).strip()

        for wh in warehouses:
            area = str(wh["Area"]).strip()
            if area == "Λάρνακα":
                availability = str(wh["AvailabilityName"]).strip()

        f_data = ["","","",sku,size,availability,"","",""]

        with open('output_90.csv', 'a', newline='', encoding="utf-8", errors="ignore") as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerow(f_data)

        print(i,r_1.status_code,r_2.status_code)
