class User:
    def __init__(self, userType):
        self.userType = userType

    def getUserType(self):
        return self.userType

    def setUserType(self, userType):
        self.userType = userType