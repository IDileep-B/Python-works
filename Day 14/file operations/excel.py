'''
import csv


with open('names.csv','r') as file:
    data = csv.reader(file)

    for row in data:
        print(row[1])
'''
'''
import csv


with open('names.csv','a', newline='\n') as file:
    data = csv.writer(file)
    data.writerow(['5','Varsha'])
'''

'''
import csv

with open('products.csv','a', newline='\n') as file:
    data = csv.writer(file)
    data.writerow(['Product_Ids','Product','Price'])
    data.writerow(['1','watch','2399'])
    data.writerow(['2','charger','499'])
    data.writerow(['3','tab','13999'])
 '''
import csv

with open('products.csv','r') as file:
    data = csv.reader(file)
    for i in data:
        print(i)
