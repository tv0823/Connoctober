from User import *

class Seeker(User):
    def __init__(self, name, city):
        super().__init__("Seeker")
        self.name = name
        self.city = city
        self.help_needed = ""

    def setHelp(self, help_text):
        self.help_needed = help_text

    def getHelp(self):
        return self.help_needed

    def getName(self):
        return self.name

    def getCity(self):
        return self.city
