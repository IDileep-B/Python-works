with  open('sample.txt','w+') as file:

    file.write("\nFile operations")
    file.seek(0)
    print(file.read())

