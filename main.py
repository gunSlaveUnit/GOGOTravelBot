from dotenv import dotenv_values

from db import DB
from bot import TelegramBot

config = dotenv_values("envs/.bot")

if __name__ == "__main__":
    database = DB()
    database.create()

    bot = TelegramBot(api_token=config["TOKEN"])
    bot.run()
