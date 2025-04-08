class HelpRequest:
    def __init__(self, requester_name, request_details, city, phone_num):
        self.requester_name = requester_name
        self.request_details = request_details
        self.city = city
        self.phone_num = phone_num

    def openRequest(self):
        return f"New request from: {self.requester_name}",f"Details: {self.request_details}",f"City: {self.city}", f"Phone: {self.phone_num}"