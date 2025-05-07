from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_buttons() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text="Start", callback_data="start"),
        InlineKeyboardButton(text="Help", callback_data="help"),
        InlineKeyboardButton(text="Settings", callback_data="settings"),
    ]
    return InlineKeyboardMarkup(inline_keyboard=[[btn] for btn in buttons])
