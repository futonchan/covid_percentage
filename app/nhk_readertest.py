import csv

path = "./static/csv/nhk_news_covid19_prefectures_daily_data.csv"

csvfile = open(path,encoding="utf-8")
prefnames = {}
for index, row in enumerate(csv.reader(csvfile)):
    if index == 0:
        continue
    row_prefname = row[2]
    row_covid_total_num = int(row[4])
    prefnames[row_prefname] = row_covid_total_num
print(prefnames)