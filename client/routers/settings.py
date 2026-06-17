from aiogram import F, types, Router

from client.keyboards.settings_menu import settings_menu, _paginate_blacklist
from core.logic.settings import Settings
from utils.config_manager import config_manager


router = Router()

@router.callback_query(F.data == 'settings_menu')
async def open_settings(callback: types.CallbackQuery):
    return await callback.message.edit_text('Выбери опцию:', reply_markup=settings_menu())

@router.callback_query(F.data == 'settings:toggle_notifications')
async def toggle_notify(callback: types.CallbackQuery):
    settings = Settings()
    await settings.toggle_notifications()
    return await callback.message.edit_text('Выбери опцию', reply_markup=settings_menu())

@router.callback_query(F.data.startswith('blacklist:page:'))
async def blacklist_open(callback: types.CallbackQuery):
    page = callback.data.split(':')[-1]
    return await callback.message.edit_text('Выбери опцию', reply_markup=_paginate_blacklist(config_manager.blacklist_buyers, page))

@router.callback_query(F.data.startswith('blacklist:rm:'))
async def blacklist_remove(callback: types.CallbackQuery):
    user_name = callback.data.split(':')[-2]
    page = callback.data.split(':')[-1]
    settings = Settings()
    await settings.toggle_user_msg_filter(user_name)
    return await callback.message.edit_text('Выбери опцию', reply_markup=_paginate_blacklist(config_manager.blacklist_buyers, page))
