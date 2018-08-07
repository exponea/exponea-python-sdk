import base64

class BasicAuth():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def get_base_token(self):
        text = bytearray("{}:{}".format(self.username, self.password), "utf-8")
        return base64.b64encode(text).decode("utf-8")
    
    def get_headers(self):
        token = self.get_base_token()
        headers = {
            "authorization": "Basic {}".format(token),
            "content-type": "application/json"
        }
        print(headers)
        return headers
