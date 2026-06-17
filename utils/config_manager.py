
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.models import BaseConfig
from fpworker.di_list import get_db


class ConfigManager:
    def __init__(self):
        self.new_message_notifications: bool = True
        self.blacklist_buyers: list = []
    
    async def load_config(self):
        '''Загрузка конфига в память при старте'''
        db: AsyncSession = await get_db()
        settings_obj = await db.execute(select(BaseConfig))
        settings = settings_obj.all()
        self.new_message_notifications = settings.new_message_notifications
        self.blacklist_buyers = settings.blacklist_buyers

config_manager = ConfigManager()