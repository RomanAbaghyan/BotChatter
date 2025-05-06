# import openai
import requests

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Update, Message

from config import settings

user_router = Router()


@user_router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        "👋 Hi, I'm *BotChatter*! Your friendly AI companion powered by DeepSeek.\n\n"
        "Just type your message and I’ll reply with answers, suggestions, or a friendly chat.\n\n"
        "_Try asking something like:_\n"
        "- What's the capital of Iceland?\n"
        "- Help me write a Python function\n"
        "- Tell me a fun fact\n\n"
        "💡 Tip: You can start chatting right away!"
    )


@user_router.message(F.text)
# @user_router.edited_message(F.text)
async def menu_cmd(message: Message):
    user_message = message.text

    headers = {
        "Authorization": f"Bearer {settings.HF_TOKEN}",
        "Content-Type": "application/json",
        "X-Title": "BotChatter",  # optional
    }

    # Define the request payload (data)
    data = {
        "model": "deepseek/deepseek-chat:free",
        "messages": [{"role": "user", "content": user_message}]
    }

    # Send the POST request to the DeepSeek API
    response = requests.post(settings.API_URL, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
    else:
        result = response.text

    if isinstance(result, dict) and len(result) > 0:
        bot_reply = result.get('choices', "Sorry, I couldn't understand that.")[0].get('message').get('content')
    else:
        bot_reply = "Error: Unable to generate a response."

    await message.answer(bot_reply)



# @user_router.message(Command('payment', 'name'))
# async def menu_cmd(message: types.Message):
#     await message.answer("Payment methods:")


# @user_router.message(Command('Shipping', 'name'))
# async def menu_cmd(message: types.Message):
#     await message.answer("Types of shipping:")
# 
# @user_router.message(F.text)
# @user_router.edited_message(F.text)
# async def menu_cmd(message: types.Message):
#     await message.answer(message.text)



