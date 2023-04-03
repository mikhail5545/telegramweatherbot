"""
Паттерны кнопок inline-клавиатуры для бота
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


BTN_WEATHER = InlineKeyboardButton('Weather', callback_data='weather')
BTN_WIND = InlineKeyboardButton('Wind', callback_data='wind')
BTN_SUN_TIME = InlineKeyboardButton('Daylight hours', callback_data='sun_time')
BTN_HUMIDITY = InlineKeyboardButton('Humidity', callback_data='humidity')
BTN_CLOUDNESS = InlineKeyboardButton('Cloudness', callback_data='cloudness')
BTN_PRESSURE = InlineKeyboardButton('Pressure', callback_data='pressure')
BTN_START = InlineKeyboardButton('Start', callback_data='start')


WEATHER = InlineKeyboardMarkup().add(BTN_WIND).add(BTN_SUN_TIME).add(BTN_HUMIDITY).add(BTN_CLOUDNESS).add(BTN_PRESSURE)
WIND = InlineKeyboardMarkup().add(BTN_WEATHER).add(BTN_WIND).add(BTN_HUMIDITY).add(BTN_CLOUDNESS).add(BTN_PRESSURE)
SUN_TIME = InlineKeyboardMarkup().add(BTN_WEATHER).add(BTN_WIND).add(BTN_HUMIDITY).add(BTN_CLOUDNESS).add(BTN_PRESSURE)
HUMIDITY = InlineKeyboardMarkup().add(BTN_WEATHER).add(BTN_WIND).add(BTN_SUN_TIME).add(BTN_CLOUDNESS).add(BTN_PRESSURE)
CLOUDNESS = InlineKeyboardMarkup().add(BTN_WEATHER).add(BTN_WIND).add(BTN_SUN_TIME).add(BTN_HUMIDITY).add(BTN_PRESSURE)
PRESSURE = InlineKeyboardMarkup().add(BTN_WEATHER).add(BTN_WIND).add(BTN_SUN_TIME).add(BTN_HUMIDITY).add(BTN_CLOUDNESS)
START = InlineKeyboardMarkup().add(BTN_WEATHER).add(BTN_WIND).add(BTN_SUN_TIME).add(BTN_HUMIDITY).add(BTN_CLOUDNESS).add(BTN_PRESSURE)
