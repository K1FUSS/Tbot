import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
API_TOKEN = '6510074950:AAE-o0-1JxZ9Ykre8qaFUpuxhJYtdrOIhMc'
# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Новый маршрут"),
            types.KeyboardButton(text="Библиотека карт")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Выберите интересующее", reply_markup=keyboard)








@dp.message(F.text.lower() == "новый маршрут")
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Официальная часть",
        callback_data="Официальная часть")
    )
    await message.answer(
        "Вот ответ на Ваш Запрос",
        reply_markup=builder.as_markup()
    )

from aiogram.utils.keyboard import InlineKeyboardBuilder

@dp.message(F.text.lower() == "библиотека карт")
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(
        text="Вот ответ на Ваш запрос",
        url="http://act1vator.tilda.ws/mospoly")
    )


    await message.answer(
        'Выберите ссылку',
        reply_markup=builder.as_markup(),
    )

@dp.callback_query(F.data == "Официальная часть")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Скоро будет ДОД")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
