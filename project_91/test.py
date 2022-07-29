import csv
urls =[]
with open('Yelp.csv', 'r' ) as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        url = str(line[0]).strip()
        if "https://www.yelp.com" in url:
            urls.append(url)
        else:
            urls.append("https://www.yelp.com"+url)
print(len(urls))
