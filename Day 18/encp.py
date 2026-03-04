class Snapchat:
    def __init__(self,username,password,friends):
        self.username = username
        self.__password = password
        self._friends = friends

    def getpassword(self):
        return self.__password
    def setpassword(self,new_password):
        self.__password = new_password

    @property
    def oprFriends(self):
        return self._friends

    @oprFriends.setter
    def oprFriends(self,newfriend):
        self._friends.append(newfriend)
        


saaketh = Snapchat('saaketh','12345',['praveen','nikhil'])

print(f'Name before modification: {saaketh.username}')
saaketh.username = 'sapnil'
print(f'Name after modification: {saaketh.username}')

print(f'password before modification: {saaketh.getpassword()}')
saaketh.setpassword('S@123')
print(f'password after modification: {saaketh.getpassword()}')

print(f'Friends after modification:{saaketh.oprFriends}()')
saaketh.oprFriends = 'abhunandhan'
print(f'Friends before modification:{saaketh.oprFriends}()')




        
