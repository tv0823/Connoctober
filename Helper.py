from User import *
class Helper(User):
    def __init__(self,helpType = []):
        super().__init__("Helper")
        self.help_types = helpType

    def updateHelp(self, operatingln):
        self.operatingln = operatingln



