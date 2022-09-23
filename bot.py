from aiogram import Bot, Dispatcher, executor, types 


class TelegramBot:
    def __init__(self, api_token: str):
        if not isinstance(api_token, str) or api_token == "":
            print("ERROR: token must be a non empty string")

        self.bot = Bot(token=api_token)
        self.dispatcher = Dispatcher(self.bot)

        self.dispatcher.register_message_handler(
                self.select_language, 
                commands=["start"]
            )

    def run(self):
        executor.start_polling(self.dispatcher)

    async def select_language(self, message: types.Message):
        await message.answer("Language selection")
