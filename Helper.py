from User import *

class Helper(User):
    def __init__(self, help_types=None):
        super().__init__("Helper")
        if help_types is None:
            help_types = []
        self.help_types = help_types
        self.operating_in = None

    def updateHelpTypes(self, help_type):
        if help_type not in self.help_types:
            self.help_types.append(help_type)

    def updateOperatingLocation(self, location):
        self.operating_in = location

    def getHelpTypes(self):
        return self.help_types

    def getOperatingLocation(self):
        return self.operating_in
