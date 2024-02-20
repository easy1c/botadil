import sqlite3
from aiogram import types, Dispatcher
import const
from config import BOT, MEDIA_DESTINATION
from database import bot_db
from keyboards import start_inline_buttons
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State ()
    age = State ()
    zodiac_sing = State()
    photo = State()

async def regisrtation_start(call: types.CallbackQuery):
    await BOT.send_message(
        chat_id=call.from_user.id,
        text = "Send me ur nickname, please!"
    )
    await RegistrationStates.nickname.set()

async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data["nickname"] = message.text


    await BOT.send_message(
        chat_id= message.from_user.id,
        text= "Send me ur bio"
    )
    await RegistrationStates.next()

def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        regisrtation_start,
        lambda call: call.data== "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state = RegistrationStates.nickname,
        content_types=["text"]
    )
























