from typing import Optional

import dotenv
import os

dotenv.load_dotenv()

class Settings:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__init__()
        return cls.__instance

    def __init__(self):
        self.BOT_TOKEN = self.get_env("BOT_TOKEN")
        self.HF_TOKEN = self.get_env("HF_TOKEN")
        self.API_URL = self.get_env("API_URL")

    def get_env(self, key: str, cast: Optional[type] = None):
        value = os.environ.get(key)
        if not value:
            raise ValueError(f'env does not have specified key "{key}"')
        if cast is not None:
            return cast(value)
        return value


settings = Settings()