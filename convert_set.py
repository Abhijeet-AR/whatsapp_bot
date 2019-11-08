import csv

inputs = []
with open('replies_data.csv') as data_file:
    reader = csv.reader(data_file)

    flag = True
    for row in reader:
        if flag:
            inputs.append(set(row))
            flag = False

        else:
            flag = True

print(*inputs)

