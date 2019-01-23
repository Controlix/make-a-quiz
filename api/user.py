import datetime

class User:
    def __init__(self, username, password, registered_on = str(datetime.datetime.now())):
        self.username = username
        self.password = password
        self.registered_on = registered_on


    @classmethod
    def fromDict(cls, dict):
        return cls(dict['username'], dict['password'])
