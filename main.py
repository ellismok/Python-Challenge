import pathlib
import csv
csvpath = pathlib.Path("Python-Challenge/Resources/PyBank/budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
