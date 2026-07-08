from fpx import FunPayTools

from utils.funpay_manager import FunPayManager
from utils.exceptions import BotError

class EventLogic:
    def __init__(self):
        self.fpx: FunPayTools = FunPayManager.get()

    async def send_message(self, chat_id, text):
        try:
            return await self.fpx.account.chat.send_message(chat_id, text)
        except Exception as e:
            raise BotError(e)

    async def refund_order(self, order_id):
        await self.fpx.account.order.refund_order(order_id)