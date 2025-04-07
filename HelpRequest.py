class HelpRequest:
    def __init__(self, requester_name, request_details, city):
        self.requester_name = requester_name
        self.request_details = request_details
        self.city = city

    def openRequest(self):
        return f"New request from: {self.requester_name}", f"Description of the request: {self.request_details}", f"City: {self.city}"