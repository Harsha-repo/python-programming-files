import csv
import pandas
with open('customers100.csv') as f:
    data = list(csv.reader(f))
    print(data[0])  
    