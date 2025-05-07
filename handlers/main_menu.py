from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.main_menu import main_menu_buttons

main_menu_router = Router()

@main_menu_router.message(CommandStart())
async def start_callback(message: Message):
    await message.answer(
        "Welcome! How can I help you today?", reply_markup=main_menu_buttons()
    )



# async def help_callback(callback_query: types.CallbackQuery):
#     await callback_query.answer()
#     await callback_query.message.answer(
#         "Here are some things I can help with:", reply_markup=help_menu_buttons()
#     )
