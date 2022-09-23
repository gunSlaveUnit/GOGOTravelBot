class TelegramBot:
    def __init__(self, api_token: str):
        if not isinstance(api_token, str) or api_token == "":
            print("ERROR: token must be a non empty string")

    def run(self):
        pass

