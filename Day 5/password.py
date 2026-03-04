pwd = input("Enter the password")

if len(pwd) >=8:
    s=set()
    for i in pwd: 
        if i.isupper():
            print("upper")
        elif i.islower():
            print("lower")
        elif i.isdigit():
            print("digit")
        else:
            print("splchar")
    if len(s)==4:
        print("strong password")
    else:
        print("weak password.password needs to have upper,lower,special character and digit")
    else:
        print("length needs to be >=8")


    

