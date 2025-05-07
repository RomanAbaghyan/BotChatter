import re
from typing import List

from aiogram.client import bot
from aiogram.enums import ParseMode
from aiogram.types import Message


def escape_markdown(text: str) -> str:
    # Escape all MarkdownV2 special characters
    escape_chars = r'_\[()~`>#+-=|{}.'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

def prepare_markdown_message(text: str) -> str:
    # Convert markdown headers to bold
    text = re.sub(r'^\s*#{1,6}\s*(.*)', r'*\1*', text, flags=re.MULTILINE)
    return escape_markdown(text)

def split_message(text: str, max_length: int = 512) -> List[str]:
    """
    Splits the message into smaller parts if it exceeds the max length.
    Tries to split at newline characters.
    """
    if len(text) <= max_length:
        return [text]

    lines = text.split('\n\n')
    chunks = []
    current_chunk = ""

    for line in lines:
        # +1 accounts for the newline character
        if len(current_chunk) + len(line) + 1 <= max_length:
            current_chunk += line + '\n\n'
        else:
            chunks.append(current_chunk.rstrip('\n'))
            current_chunk = line + '\n\n'

    if current_chunk:
        chunks.append(current_chunk.rstrip('\n'))

    return chunks


async def send_message(message: Message, bote_reply: str, parse_mode: ParseMode = ParseMode.MARKDOWN):
    replies = split_message(bote_reply)

    for reply in replies:
        await message.answer(reply, parse_mode=parse_mode)

    # await message.answer(prepare_markdown_message(bot_reply), parse_mode=ParseMode.MARKDOWN)
    # await message.answer(bot_reply, parse_mode=ParseMode.MARKDOWN)


