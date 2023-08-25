import os
from pathlib import Path
from typing import List

from aiogram.types import ReplyKeyboardMarkup
from os.path import join as join_path




BTN_CATOLOG="каталоги"
BTN_FEEDBACK="подключиться к администратору"
BTN_BACK="назад"


BTN_CONTROLLER="контролеры"
BTN_INVERTOR="инверторы"
BTN_PANELS="панели"
BTN_BATTERY="аккумулятор"


def main():
    row1: List=[BTN_CATOLOG,BTN_FEEDBACK]
    keyboard: List=[row1,]
    markup=ReplyKeyboardMarkup(resize_keyboard=True,keyboard=keyboard)
    return markup


def feedback():
    row1: List=[BTN_BACK]
    keyboard: List=[row1]
    markup=ReplyKeyboardMarkup(resize_keyboard=True,keyboard=keyboard)
    return markup

def catologs():
    # row1: List=[BTN_CONTROLLER]
    row1: List=[BTN_BATTERY]
    row2: List=[BTN_INVERTOR]
    row3: List=[BTN_PANELS]
    row4: List=[BTN_BACK]
    keyboard: List=[row1,row2,row3,row4]
    markup=ReplyKeyboardMarkup(resize_keyboard=True,keyboard=keyboard)
    return markup


