import asyncio
import hashlib
import os
from os.path import join as join_path
from pathlib import Path
import shutil

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
import requests
from aiogram import types
from states import FeedBackState
import aiogram
from dispatch import dp, bot
# from services import write_user
from services.config import *
from buttons.markup import BTN_CATOLOG, BTN_FEEDBACK,feedback,BTN_BACK,catologs
from states import FeedBackState,CatologState
from configs.constants import FEEDBACK_ID
from services import about_catolog


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def echo_message(message: types.Message):
    if message.text==BTN_CATOLOG:
        await states.CatologState.catologs.set()
        await message.bot.send_message(chat_id=message.chat.id,text="каталоги:",reply_markup=catologs())
    if message.text==BTN_FEEDBACK:
        await states.FeedBackState.feeedback.set()
        await message.bot.send_message(chat_id=message.chat.id,text="Вы выбрали пост администратора. Напишите свое мнение!",reply_markup=feedback())
    if message.text==BTN_BACK:
        await message.bot.send_message(chat_id=message.chat.id,text="выбирать",reply_markup=main())

@dp.message_handler(state=FeedBackState.feeedback)
async def feedback_handler(message: types.Message, state: FSMContext):
    try:
        if not message.text==BTN_BACK:
            await message.bot.send_message(chat_id=FEEDBACK_ID,text=f"у вас новое сообщение: {message.text}")
            await message.answer(text="Ваше сообщение было отправлено, выбирать!")
        else:
            await state.finish()
            await message.bot.send_message(chat_id=message.chat.id,text="выбирать!",reply_markup=main())
        
    except Exception as err:
        print(err)
        pass
@dp.message_handler(state=CatologState.catologs)
async def catologs_handler(message: types.Message, state: FSMContext):
    try:
        if not message.text==BTN_BACK:
            await about_catolog(message)
        else:
            await state.finish()
            await message.bot.send_message(chat_id=message.chat.id,text="выбирать!",reply_markup=main())
        
    except Exception as err:
        print(err)
        pass





















