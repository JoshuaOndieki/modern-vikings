class User (object):
    users = {}

    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type

    def create(self):
        User.users.append (self)

    def delete(self):
        User.users.remove (self)



