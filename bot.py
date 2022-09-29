from aiogram import Bot, Dispatcher, executor

from keyboard import Keyboard


class TelegramBot:
    def __init__(self, api_token: str):
        if not isinstance(api_token, str) or api_token == "":
            print("ERROR: token must be a non empty string")

        self.bot = Bot(token=api_token)
        self.dispatcher = Dispatcher(self.bot)

        self.choose_language_inline_keyboard = Keyboard([u'English', u'Русский', u'Deutsch'])

        self.dispatcher.register_message_handler(
                self.choose_language_inline_keyboard.select_language,
                commands=["start"]
            )

        self.dispatcher.register_callback_query_handler(self.choose_language_inline_keyboard.language_chosen_callback)

    def run(self):
        executor.start_polling(self.dispatcher)
