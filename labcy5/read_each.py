import csv
with open('username.csv',newline="")as csvfile:
    data=csv.reader(csvfile,delimiter=';',quotechar='|')
    for row in data:
        print(row)


