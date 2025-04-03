from User import *
class HelpRequest:
    def init(self, requester_name, request_details):
        self.requester_name = requester_name
        self.request_details = request_details

    def openRequest(self):
        print(f"בקשה חדשה מ: {self.requester_name}")
        print(f"תיאור הבקשה: {self.request_details}")
