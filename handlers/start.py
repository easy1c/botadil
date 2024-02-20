from aiogram import types, Dispatcher
import const
from config import BOT
from database import bot_db
from keyboards import start_inline_buttons



async def start_button(message: types.Message):
    db = bot_db.Database()
    db.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    # await BOT.send_message(
    #     chat_id=message.from_user.id,
    #     text=const.START_MENU_TEXT.format(
    #     user = message.from_user.first_name
    #     ),
    #     reply_markup=await start_inline_buttons.start_keyboard()
    # )
    with open('/Users/adilbekbazarov/PycharmProjects/TG_bot/media/hi.gif', 'rb') as ani:
        await BOT.send_animation(
            chat_id=message.from_user.id,
            animation=ani,
            caption=const.START_MENU_TEXT.format(
                user=message.from_user.first_name
            ),
            reply_markup=await start_inline_buttons.start_keyboard()  # Исправлена опечатка здесь
        )


    # with open(MEDIA_DESTINATION + 'bot.jpeg', 'rb') as photo:
    #     await BOT.send_photo(
    #         chat_id=message.from_user.id,
    #         photo=photo,
    #         caption=const.START_MENU_TEXT.format(
    #             user=message.from_user.first_name
    #         ),
    #         reply_markup=await start_inline_buttons.start_keyboard()  # Исправлена опечатка здесь
    #     )

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_button,
        commands=['start']
    )