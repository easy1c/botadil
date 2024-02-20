from aiogram import types, Dispatcher
import datetime
import database.bot_db
from config import BOT, GROUP_ID
from keyboards import questionnaire_inline_buttons
from profanity_check import predict, predict_prob

async def chat_message(message: types.Message):
    db=database.bot_db.Database()
    if message.chat.id == int(GROUP_ID):
        ban_words_prob = predict_prob([message.text])
        if ban_words_prob > 0.8:
            potential = db.sql_select_ban_user(
                tg_id=message.from_user.id
            )

            if not potential:
                db.sql_insert_ban_user(
                    tg_id=message.from_user.id
                )
            elif potential['count'] >=3:
                # await BOT.ban_chat_member(
                #     chat_id=message.chat.id,
                #     user_id=message.from_user.id,
                #     until_date=datetime.datetime.now()+datetime.timedelta(hours = 1)
                # )
                await BOT.send_message(
                    chat_id=message.chat.id,
                    text=f"User = {message.from_user.first_name} banned\n"
                         f"Ban Count: {potential['count']}"
                )
            else :
                db.sql_insert_ban_user(
                    tg_id=message.from_user.id
                )

            db.sql_insert_ban_user(
            tg_id= message.from_user.id
            )
            await message.delete()
            await BOT.send_message (
                chat_id=message.chat.id ,
                text=f"Hello {message.from_user.first_name} \n"
                     f"Sogunbo Nahui"

            )

def register_group_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(
        chat_message,
    )