class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def fromDict(cls, dict):
        return cls(dict['username'], dict['password'])
