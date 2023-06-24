import csv

with open("inferences.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    row = next(reader)
    print(row[6])