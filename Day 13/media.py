media = ['beach.png','waves.mp4','mountain.jpg',
         'party.jpg','dance.mp4','selfie.png','birthday.png','concert.jpg',
         'singing.mp4','sunset.jpeg','trip..jpg']
photos =[]
videos =[]
for i in media:
    if i.endswith('.mp4'):
        videos.append(i)
    else: 
        photos.append(i)
print('\n----------photos---------')
for i in photos:
    print(i)
print('\n----------videoss---------')
for i in videos:
    print(i)

select = set(input("Enter the files to share(using comma):").split(','))
for i in select:
    if i in media:
        print(f'{i}-sent)')
    else:
        print(f'{i}-file not found')
        
                 
        
         
