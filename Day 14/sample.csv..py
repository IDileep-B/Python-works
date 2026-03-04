import csv

with  open('names.csv','r') as file:

   content = csv.reader(file)
   for i in content:
        print(i)
