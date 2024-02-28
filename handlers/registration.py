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
    auto = State()

async def regisrtation_start(call: types.CallbackQuery):
    await BOT.send_message(
        chat_id=call.from_user.id,
        text = "Send me ur nickname, please!"
    )
    await RegistrationStates.nickname.set()


# ------------------------------------------------------------
async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data["nickname"] = message.text
        print(data)

    await BOT.send_message(
        chat_id= message.from_user.id,
        text= "Send me ur bio"
    )
    await RegistrationStates.next()

async def load_auto(call: types.CallbackQuery):
        await BOT.send_message(
            chat_id=call.from_user.id,
            text="tell me your favorite car brand!"
        )
        await RegistrationStates.auto()
# ---------------------------------------------------------
async def load_bio(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data["bio"] = message.text
        print (data)

    await BOT.send_message(
        chat_id= message.from_user.id,
        text = "How old r u ?\n"
               "(Send me only numeric text\n"
               "Example for dalbaebs: 15-19-22)"

    )

    await RegistrationStates.next()
# ----------------------------------------------------------------
async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        int(message.text)
    except ValueError:
        await BOT.send_message(
        chat_id= message.from_user.id,
        text = "I told you nahui send me ONLY numeric text blyat\n"
               "Registration failed🚫\n"
               "Restart registration!!!"
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age']= int(message.text)
        print(data)
# ----------------------------------------------------------------
    await BOT.send_message(
        chat_id= message.from_user.id,
        text = 'Now send me ur zodiac sing'
    )
    await RegistrationStates.next()

async def load_zodiac_sing(message:types.Message,
                           state: FSMContext):
    async with state.proxy()as data:
        data['sing'] = message.text
        print(data)
# ----------------------------------------------------------------------
    await BOT.send_message(
        chat_id=message.from_user.id,
        text="Send me ur photo\n"
             "Only in photo format"
    )
    await RegistrationStates.next()

async def load_photo(message: types.Message,
                     state: FSMContext):
    db= bot_db.Database()
    path = await message.photo[-1].download(
        destination_dir= MEDIA_DESTINATION
    )
    async with state.proxy() as data:
        db.sql_insert_profile(
            tg_id = message.from_user.id,
            nickname=data['nickname'],
            bio=data['bio'],
            age=data['age'],
            sing=data['sing'],
            photo=path.name,
        )

        with open(path.name, "rb") as photo:
            await BOT.send_photo(
                # chat_id=message,
                chat_id=message.from_user.id,
                photo = photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    bio=data['bio'],
                    age=data['age'],
                    sing=data['sing'],
                )
            )
    await BOT.send_message(
            chat_id=message.from_user.id,
            text= "U have successfully register✅\n"
                  "Pozdravlena!!!"
    )
    await state.finish()

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
    dp.register_message_handler(
        load_auto,
        state=RegistrationStates.auto,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_bio,
        state=RegistrationStates.biography,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_zodiac_sing,
        state=RegistrationStates.zodiac_sing,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )


