import csv
with open(f'output_91.csv', 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        c_1 = str(line[0])
        c_2 = str(line[1])
        c_3 = str(line[2])
        c_4 = str(line[3])
        c_5 = str(line[4])
        try:
            c_6 = str(line[5])
        except:
            c_6 = ""

        if c_2=="":
            print(True)

            with open(f'unscraped_urls.csv', 'a', newline='', encoding="utf-8") as new_file:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow([c_1])
