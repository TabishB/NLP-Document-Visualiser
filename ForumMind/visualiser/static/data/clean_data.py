import csv

listData = []
with open('topic_words1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        listData.append(row)


splitData = []
for data in listData[0]:
    splitData.append(data.split(','))
# print(listData[0][0].split(','))
for data in splitData:
    print(data)

with open('topic1_cleaned.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for d in splitData:
        writer.writerow(d)
