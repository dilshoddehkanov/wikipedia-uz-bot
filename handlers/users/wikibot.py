from aiogram import types

from loader import dp


@dp.message_handler()
async def sndWiki(message: types.Message):
    try:
        if message.text.title() == 'Dilshod':
            await message.reply('Ha men Dehkanov Dilshodman')
        else:
            respond = wikipedia.summary(message.text)
            await message.answer(respond)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi')