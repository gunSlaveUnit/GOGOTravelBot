from dotenv import dotenv_values

from bot import TelegramBot

config = dotenv_values(".env")

if __name__ == "__main__":
    bot = TelegramBot(api_token=config["TOKEN"])
    bot.run()
