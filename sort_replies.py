import csv

data = []
with open('replies_data.csv') as data_file:
    reader = csv.reader(data_file)
    for row in reader:
        data.append(row)

with open('replies_data.csv', 'w') as data_file:
    writer = csv.writer(data_file, delimiter=',')
    for row in data:
        writer.writerow(sorted(filter(lambda x: x != '', row)))
