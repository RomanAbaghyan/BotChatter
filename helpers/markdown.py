import re

def escape_markdown(text: str) -> str:
    # Escape all MarkdownV2 special characters
    escape_chars = r'_\[()~`>#+-=|{}.'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

def prepare_markdown_message(text: str) -> str:
    # Convert markdown headers to bold
    text = re.sub(r'^\s*#{1,6}\s*(.*)', r'*\1*', text, flags=re.MULTILINE)
    return escape_markdown(text)