import User from *
class Helper(User):
    def __init__(self,helpType = []):
        self.help_types = helpType
    def updateHelp(self, operatingln):
        self.operatingln = operatingln



