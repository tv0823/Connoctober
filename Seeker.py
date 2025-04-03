from User import User
class Seeker(User):
    def __init__(self, city):
        super().__init__("Seeker")
        self.city = city
