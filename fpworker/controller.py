from fpx import Message

from utils.config_manager import config_manager


class FunPayController:
    @staticmethod
    async def MessageManager(message: Message) -> bool:
        '''Фильтр обработки сообщений'''
        if not config_manager.new_message_notifications:
            return False
        if message.sender in config_manager.blacklist_buyers:
            return False
        return True


controller = FunPayController()