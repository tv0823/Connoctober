class HelpRequest:
    def __init__(self, requester_name, request_details):
        self.requester_name = requester_name
        self.request_details = request_details

    def openRequest(self):
        print(f"New request from: {self.requester_name}")
        print(f"Description of the request: {self.request_details}")

