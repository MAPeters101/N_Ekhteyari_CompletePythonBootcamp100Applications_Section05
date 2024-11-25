import csv

data = [
    ['Name','Age','City'],
    ['Alice',25,'New York'],
    ['Bob',45,'San Francisco'],
    ['Charlie',15,'Los Angeles'],
]

with open('file040.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

with open('file040.csv', 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

