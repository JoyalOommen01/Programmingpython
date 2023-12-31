import csv
with open('name.csv',newline="")as csvfile:
    data = csv.DictReader(csvfile)
    print("name and age")
    print("---------------------------------")
    for col in data:
        print(col['name'],col['age'])
