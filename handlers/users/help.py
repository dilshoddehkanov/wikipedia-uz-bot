from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "Yana yordam kerak bo'lsa adminga murojaat qiling: @Web_developper_D")
    
    await message.answer("\n".join(text))
