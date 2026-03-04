'''
with open('sample.txt','r') as file:
    content = file.read()
    print(content)
'''

'''
with open('sample.txt','w') as file:
    file.write('Override')
'''

with open('sample.txt','a') as file:
    file.write('Override')
    
