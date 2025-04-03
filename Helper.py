import User from *
class Helper(User):
    def __init__(self,helpType = None):
        if helpType is None:
            self.help_types = []
        else:
            self.help_types = helpType
    def updateHelp(self, operatingln):
        self.operatingln = operatingln



