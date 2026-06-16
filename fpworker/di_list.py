

from core.database.engine import Session


async def get_db(event):
    async with Session() as db:
        return db