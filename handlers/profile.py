import sqlite3
import const
from aiogram import types, Dispatcher
from config import BOT
from const import PROFILE_TEXT
from database.bot_db import Database
async def my_profile_call(call: types.CallbackQuery):
    db= Database()
    profile = db.sql_select_profile(
        tg_id=call.from_user.id
    )

    if profile:
        with open(profile['photo'], 'rb' ) as photo:
            await BOT.send_photo(
                await BOT.send_photo(
                    chat_id=call.from_user.id,
                    photo=photo,
                    caption=const.PROFILE_TEXT.format(
                        nickname=profile['nickname'],
                        bio=profile['bio'],
                        age=profile['age'],
                        sing=profile['sing'],
                    )
                )
            )
    else:
        await BOT.send_message(
            chat_id=call.from_user.id,
            text= "U did not registered\n"
                  "Please register to view ur profile"
        )

def register_profile_handler(dp:Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
        )
