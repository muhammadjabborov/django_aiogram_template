from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def build_contact_request_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton(text="Share phone number", request_contact=True))
    return keyboard

