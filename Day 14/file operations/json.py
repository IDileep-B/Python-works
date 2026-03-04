'''
import json

with open('demo.json','w') as file:
    data =[
    {'id':'1','name':'saaketh'},
    {'id':'2','name':'ravi'},
    {'id':'3','name':'abid'},
    {'id':'4','name':'dileep'},
    {'id':'5','name':'abi nandhan'},
    ]
    json.dump(data,file,indent=4)
    print("data saved successfully")
'''

import json

with open('demo.json',"r") as file:
    data = json.load(file)

data.append({'id':'6','name':'varsha'})

with open('demo.json',"w") as file:
    json.dump(data,file,indent=4)
