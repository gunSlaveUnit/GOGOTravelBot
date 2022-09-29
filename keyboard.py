from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message


class Keyboard:
    def __init__(self, button_titles: List[str]):
        self.layout = InlineKeyboardMarkup()

        for title in button_titles:
            inline_keyboard_button = InlineKeyboardButton(text=title, callback_data=title)
            self.layout.add(inline_keyboard_button)

    async def select_language(self, message: Message):
        await message.answer("Please, choose your language:", reply_markup=self.layout)

    async def language_chosen_callback(self, call: CallbackQuery):
        await call.message.answer(f"Chosen language: {call.data}. You can change it at any time")
