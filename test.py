import csv
# def writecsv(data):
#     with open("data.csv","a",newline="",encoding="utf-8") as file:
#         fw = csv.writer(file)
#         fw.writerow(data)
# writecsv()

with open("data.csv",newline="",encoding="utf-8") as file:
    fr = list(csv.reader(file))
    print(fr)
