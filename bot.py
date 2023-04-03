"""
Инициализация бота и хендлеров
"""
import logging
from aiogram import Bot, Dispatcher, executor, types

import bot_inline_keyboard
import messages
import bot_config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def show_weather(message: types.Message):
    await message.answer(text='Choose the option below:', reply_markup=bot_inline_keyboard.START)


@dp.message_handler(commands='weather')
async def show_weather(message: types.Message):
    await message.answer(text=await messages.weather(), reply_markup=bot_inline_keyboard.WEATHER)


@dp.message_handler(commands='wind')
async def show_wind(message: types.Message):
    await message.answer(text=await messages.wind(), reply_markup=bot_inline_keyboard.WIND)


@dp.message_handler(commands='sun_time')
async def show_sun_time(message: types.Message):
    await message.answer(text=await messages.sun_time(), reply_markup=bot_inline_keyboard.SUN_TIME)


@dp.message_handler(commands='humidity')
async def show_sun_time(message: types.Message):
    await message.answer(text=await messages.humidity(), reply_markup=bot_inline_keyboard.HUMIDITY)


@dp.message_handler(commands='cloudness')
async def show_sun_time(message: types.Message):
    await message.answer(text=await messages.cloudness(), reply_markup=bot_inline_keyboard.CLOUDNESS)


@dp.message_handler(commands='pressure')
async def show_sun_time(message: types.Message):
    await message.answer(text=await messages.pressure(), reply_markup=bot_inline_keyboard.PRESSURE)


@dp.callback_query_handler(text='start')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, reply_markup=bot_inline_keyboard.START)


@dp.callback_query_handler(text='weather')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text=await messages.weather(), reply_markup=bot_inline_keyboard.WEATHER)


@dp.callback_query_handler(text='wind')
async def process_callback_wind(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text=await messages.wind(), reply_markup=bot_inline_keyboard.WIND)


@dp.callback_query_handler(text='sun_time')
async def process_callback_sun_time(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text=await messages.sun_time(), reply_markup=bot_inline_keyboard.SUN_TIME)  


@dp.callback_query_handler(text='humidity')
async def process_callback_humidity(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text=await messages.humidity(), reply_markup=bot_inline_keyboard.HUMIDITY)


@dp.callback_query_handler(text='cloudness')
async def process_callback_cloudness(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text=await messages.cloudness(), reply_markup=bot_inline_keyboard.CLOUDNESS) 


@dp.callback_query_handler(text='pressure')
async def process_callback_pressure(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text=await messages.pressure(), reply_markup=bot_inline_keyboard.PRESSURE)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)