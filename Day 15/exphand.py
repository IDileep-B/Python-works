'''
try:
     a=[1,2,3]
     print(a[8])
        
except (NameError,ValueError,TypeError,IndexError,ZeroDivisionError,KeyError) as e:
    print('Error Occured:{e}')
    
else:
    print('No Errors')

finally:
    print("End of the block")
'''
'''
try:
     a=int(input())
     print(a[4])
        
except Exception as e:
    print(f'Error Occured:{e}')
    
else:
    print('No Errors')

finally:
    print("End of the block")
'''

try:
    a=int(input())
    if a<0:
        raise Exception("Enter the positive Value")
        
except Exception as e:
    print(f'Error Occured:{e}')
    
else:
    print('No Errors')

finally:
    print("End of the block")

