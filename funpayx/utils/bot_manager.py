from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

class BotManager:
    _instance: Bot | None = None

    @classmethod
    def init(cls, token: str, proxy: str | None = None):
        session = AiohttpSession(proxy=proxy) if proxy else None
        cls._instance = Bot(token=token, session=session)

    @classmethod
    def get(cls) -> Bot:
        if cls._instance is None:
            raise RuntimeError("Бот не инициализирован")
        return cls._instance

class DpManager:
    _instance: Dispatcher | None = None

    @classmethod
    def init(cls):
        cls._instance = Dispatcher()

    @classmethod
    def get(cls) -> Dispatcher:
        if cls._instance is None:
            raise RuntimeError("Диспетчер не инициализирован")
        return cls._instance