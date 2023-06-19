from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from lexicon import LEXICON_RU


# Этот хэндлер срабатывает на команду /start
@dp.message(CommandStart())
async def process_start_command(msg: Message):
    await msg.answer(text=LEXICON_RU["/start"])


# Этот хэндлер срабатывает на команду /help
@dp.message(Command(commands="help"))
async def process_start_command(msg: Message):
    await msg.answer(text=LEXICON_RU["/help"])
