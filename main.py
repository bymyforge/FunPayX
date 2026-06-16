import logging
import asyncio

from bot import botmain
from funpay_listener import funpaymain

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger("httpx").setLevel(logging.WARNING)

async def main():
    logging.info('Запускаем все слушатели')
    await asyncio.gather(
        botmain(),
        funpaymain()
    )

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Бот выключен')