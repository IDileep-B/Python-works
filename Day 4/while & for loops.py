'''
i=1
while i<=10:
    print(i)
    i=i+1
'''
moves = 15
winning_point = int(input("Tell me how me moves is required to win "))

while moves >= 1:
    if 15 - winning_point== moves:
        print("You won the game")
        break
    print(f"{moves} are  left")
    moves-=1

else:
  print("Game over")
        
