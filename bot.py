from aiogram import Bot, Dispatcher

from aiogram.types import Message

import asyncio

from config_data.config import get_config, Config

from handlers import game_handlers, player_handlers

async def main() -> None:
    config: Config = get_config(None)

    bot: Bot = Bot(config.tg_bot.token_bot)

    dp: Dispatcher = Dispatcher()

    dp.include_router(game_handlers.router)
    dp.include_router(player_handlers.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    
if __name__ == "__main__":
    asyncio.run(main())





