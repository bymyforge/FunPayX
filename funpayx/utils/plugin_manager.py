import importlib.util
import sys
import json
from pathlib import Path
from aiogram import Router as AioRouter
from aiogram import F
from fpx import Router as FpxRouter
from .bot_manager import DpManager, BotManager
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def back_to_plugin_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data='plugins',
            style='danger'
        )
    )
    return builder.as_markup()

plugin_data = {
    "routers": [
        "main.router"
    ],
    "manifest": {
        "title": "TemplatePlugin",
        "description": "Шаблон оформления плагина, заполни plugin.json",
        "version": "1.0.0",
        "credits": [
            "@sanyalca"
        ],
        "custom_menu": False
    }
}

plugin_callback_list = []

router = AioRouter()

def load_router(router, manifest, id):
    plugin_callback_list.append({'id': id, 'title': manifest['title']})
    async def dynamic_handler(callback):
        await callback.message.edit_text(
            f'{manifest['title']}\n'
            f'{manifest['description']}\n'
            f'{manifest['version']}\n'
            f'{manifest['credits']}',
            reply_markup=back_to_plugin_menu()
        )
    if not manifest['custom_menu']:
        router.callback_query.register(dynamic_handler, F.data == f'plugin_{id}')

plugins_dir = Path('plugins')

def load_plugins(fp):
    plugins_dir.mkdir(parents=True, exist_ok=True)
    if plugins_dir.exists():
        dp = DpManager.get()
        plugin_id = 1
        for p_fol in plugins_dir.iterdir():
            if p_fol.is_dir():
                config_file = p_fol / 'plugin.json'
                if not config_file.exists():
                    with open(config_file, "w", encoding="utf-8") as f:
                        json.dump(plugin_data, f, ensure_ascii=False, indent=2)
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                routers_paths = config.get('routers', [])
                if isinstance(routers_paths, str):
                    routers_paths = [routers_paths]
                for r_path in routers_paths:
                    *file_parts, router_var_name = r_path.split('.')
                    file_rel_path = Path(*file_parts).with_suffix('.py')
                    router_file = p_fol / file_rel_path
                    if router_file.exists():
                        sub_module_name = '.'.join(file_parts)
                        module_name = f'plugins.{p_fol.name}.{sub_module_name}'
                        spec = importlib.util.spec_from_file_location(module_name, router_file)
                        module = importlib.util.module_from_spec(spec)
                        sys.modules[module_name] = module
                        spec.loader.exec_module(module)
                        plugin_router = getattr(module, router_var_name)
                        if isinstance(plugin_router, FpxRouter):
                            fp.router.include_router(plugin_router)
                        elif isinstance(plugin_router, AioRouter):
                            dp.include_router(plugin_router)
                manifest = config.get('manifest')
                load_router(router, manifest, plugin_id)
                plugin_id += 1
        dp.include_router(router)