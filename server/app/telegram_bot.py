import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from faststream.rabbit import RabbitBroker

TOKEN = "6251377163:AAGHocnHBFunewuf0S_D3aOexRfkhxCIsSo"
# TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher()

bot = Bot(token=TOKEN)
broker = RabbitBroker()


@broker.subscriber("orders")
async def handle_message(data: str):
    await bot.send_message(chat_id=1753986163, text=data)
    return data


# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


async def main() -> None:
    async with broker:
        await broker.start()
        logging.info("Брокер стартовал")
        await dp.start_polling(bot)
    logging.info("Конец")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
