import os
import csv


cwd = os. getcwd()
od  = cwd + "\outputs"
os.chdir(od)


files = os.listdir(od)
h_data = ["Url","Name","Address","Phone","Website","Amenities"]
with open(f'{cwd}\output_91.csv', 'w', newline='', encoding="ansi", errors="ignore") as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(h_data)
n=0
for file in files:
    try:
        with open(f'{file}', 'r', encoding="utf-8") as csv_file:
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
                # c_7 = str(line[6])
                # c_8 = str(line[7])
                # c_9 = str(line[8])
                # c_10 = str(line[9])
                # c_11 = str(line[10])
                # c_12 = str(line[11])
                # c_13 = str(line[12])
                # c_14 = str(line[13])
                # c_15 = str(line[14])
                # c_16 = str(line[15])
                # c_17 = str(line[16])
                # c_18 = str(line[17])
                # c_19 = str(line[18])
                # c_20 = str(line[19])
                # c_21 = str(line[20])
                # c_22 = str(line[21])
                # c_23 = str(line[22])
                # c_24 = str(line[23])
                # try:
                #     c_25 = str(line[24])
                # except:
                #     c_25 = ""

                data = [c_1, c_2, c_3, c_4, c_5, c_6]#, c_7, c_8, c_9, c_10, c_11, c_12, c_13, c_14, c_15, c_16, c_17, c_18, c_19, c_20, c_21, c_22, c_23, c_24, c_25]
                with open(f'{cwd}\output_91.csv', 'a', newline='', encoding="ansi", errors="ignore") as new_file:
                    csv_writer = csv.writer(new_file)
                    csv_writer.writerow(data)

    except:
        continue
    n+=1
    print(n)
