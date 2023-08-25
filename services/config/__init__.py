

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

import states
from buttons.markup import main

from dispatch import dp



@dp.message_handler(commands="start")
async def start(message: types.Message, state: FSMContext):
    chat_id=message.chat.id
    message_body = f"""
            Assalomu alaykum! \n erasolar.uz botiga xush kelibsiz!!! {chat_id}
    """


    

    await message.bot.send_message(chat_id=message.chat.id,text=message_body,reply_markup=main())


@dp.message_handler(commands="help")
async def help(message: types.Message):
    message_body = "aloqa uchun: +998995913728"
    await message.reply(message_body)


# @dp.message_handler(commands=['admin'])
# async def admin_handler(message: types.Message):
#     print(message.from_user.id)
#     markup = ReplyKeyboardRemove()
#     await sign_admin()
#     await message.answer('Parolni yozing', reply_markup=markup)
