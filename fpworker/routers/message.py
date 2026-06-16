from fpx import Router, Message, Dependency
from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession

from fpworker.di_list import get_db
from core.logic.chat import ChatLogic

router = Router()

@router.on_message()
async def get_base_msg(message: Message, db: AsyncSession = Dependency(get_db)):
    chat = ChatLogic(db)
    await chat.message_all_users(f'Пришло сообщение\n{message}')