import os
from os.path import join as join_path
from pathlib import Path
import shutil
from aiogram import types

BASE_URL = Path(__file__).parent.parent

# from states import KafedraStates, ScheduleState, FeedbackStates, AuthAdminStates
import json
from configs.constants import invertor_info,controller_info,solar_panel_info,battery_info
from buttons.markup import BTN_CONTROLLER,BTN_INVERTOR,BTN_PANELS,BTN_BATTERY

#function lar

async def about_catolog(message: types.Message):
    if message.text==BTN_BATTERY:
        path=join_path(BASE_URL,"db","battery")
        info_list=battery_info
    if message.text==BTN_INVERTOR:
        path=join_path(BASE_URL,"db","invertors")
        info_list=invertor_info
    if message.text==BTN_PANELS:
        path=join_path(BASE_URL,"db","panels")
        info_list=solar_panel_info
    try:
        for i in info_list:
            smth=i[0]+".png"
            with open(join_path(path,smth), 'rb') as photo:
                await message.answer_photo(photo, caption=f'{i[1]}\ncode:{i[0]} \n\nITEM NAME: {i[2]}')
    except Exception as err:
        print(err)
        pass
        



