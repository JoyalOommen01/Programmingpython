import csv

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

with open('my_data.csv', 'w', newline='') as csvfile:
    fieldnam = list(my_dict.keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnam)
    writer.writeheader()
    writer.writerow(my_dict)

with open('my_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
