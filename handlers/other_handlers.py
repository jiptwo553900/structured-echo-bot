from aiogram import Router
from aiogram.types import Message
from lexicon import LEXICON_RU

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(msg: Message):
    try:
        await msg.send_copy(chat_id=msg.chat.id)
    except TypeError:
        await msg.answer(text=LEXICON_RU["no_echo"])
