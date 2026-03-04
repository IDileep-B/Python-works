data ={
      'dileep@gmail.com':'Dp123@',
      'raju@gmail.com':'Raj@000',
      'monark@gmail.com':'Monk@111',
      'meetmeincanteen@gmail.com':'Meet@222',
      'hplaptop@gmail.com':'Hrx@000'
      }
print('1.Register')
print('2. Login')


   ch==1:
       email=input("Enter the email: ")
       pwd = input("Enter the password: ")
       if email in data:
           print(f"Register - failed\n{email} is already exists ")
           else:
               data[email]
