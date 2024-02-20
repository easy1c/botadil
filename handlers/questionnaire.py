from aiogram import types, Dispatcher
from config import BOT
from keyboards import questionnaire_inline_buttons


async def questionnaire_start(call: types.CallbackQuery):
    await BOT.send_message(
        chat_id= call.from_user.id,
        text= 'Python🐍 or Mojo🫀 ?',
        reply_markup= await questionnaire_inline_buttons.python_questionnaire_keyboard()
    )
    await BOT.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

# --------------------------------------------------------------

async def qq_start(call: types.CallbackQuery):
    await BOT.send_message(
        chat_id= call.from_user.id,
        text= 'Dota2 or LOL ?',
        reply_markup= await questionnaire_inline_buttons.dota_questionnaire_keyboard()
    )
    await BOT.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

async def dota_answer(call: types.CallbackQuery):
    await call.message.delete()
    await BOT.send_message(
        chat_id=call.from_user.id,
        text="You are the best"
    )

async def LOL_answer(call: types.CallbackQuery):
    await call.message.delete()
    await BOT.send_message(
        chat_id=call.from_user.id,
        text="Fucking gay"
    )
# ---------------------------------------------------------
async def auto_start(call: types.CallbackQuery):
    await BOT.send_message(
        chat_id= call.from_user.id,
        text= 'Mercedes Benz or BMW ?',
        reply_markup= await questionnaire_inline_buttons.auto_questionnaire_keyboard()
    )
    await BOT.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

async def mers_answer(call: types.CallbackQuery):
    await call.message.delete()
    await BOT.send_message(
        chat_id=call.from_user.id,
        text="GOOD"
    )

async def bmw_answer(call: types.CallbackQuery):
    await call.message.delete()
    await BOT.send_message(
        chat_id=call.from_user.id,
        text="GOOD TOO"
    )

# -----------------------------------------------------------------------------

async def phone_start(call: types.CallbackQuery):
    await BOT.send_message(
        chat_id= call.from_user.id,
        text= 'IOS or Android ?',
        reply_markup= await questionnaire_inline_buttons.phone_questionnaire_keyboard()
    )
    await BOT.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

async def ios_answer(call: types.CallbackQuery):
    await call.message.delete()
    await BOT.send_message(
        chat_id=call.from_user.id,
        text="You are rich"
    )

async def android_answer(call: types.CallbackQuery):
    await call.message.delete()
    await BOT.send_message(
        chat_id=call.from_user.id,
        text="Like"
    )
# -------------------------------------------------------------------------------
async def python_answer(call: types.CallbackQuery):
    await call.message.delete()
    await BOT.send_message(
        chat_id=call.from_user.id,
        text="Good stay in python"
    )
async def mojo_answer(call: types.CallbackQuery):
    await call.message.delete()
    await BOT.send_message(
        chat_id=call.from_user.id,
        text="Dont lie Mojo in alpha"
    )


async def yes_python_answer(call: types.CallbackQuery):
    await call.message.delete()
    await BOT.send_message(
        chat_id=call.from_user.id,
        text="Dont betray Python!"
    )


async def no_python_answer(call: types.CallbackQuery):
    await call.message.delete()
    await BOT.send_message(
        chat_id=call.from_user.id,
        text="Cool, stay in python"
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start,
        lambda call: call.data == "start_questionnaire"
    )
    dp.register_callback_query_handler(
        dota_answer,
        lambda call: call.data == "dota"
    )
    dp.register_callback_query_handler(
        LOL_answer,
        lambda call: call.data == "LOL"
    )
    dp.register_callback_query_handler(
        qq_start,
        lambda call: call.data == "choice"
    )
    dp.register_callback_query_handler(
        python_answer,
        lambda call: call.data == "python"
    )
    dp.register_callback_query_handler(
        mojo_answer,
        lambda call: call.data == "mojo"
    )
    dp.register_callback_query_handler(
        yes_python_answer,
        lambda call: call.data == "yes_python"
    )
    dp.register_callback_query_handler(
        no_python_answer,
        lambda call: call.data == "no_python"
    )
    dp.register_callback_query_handler(
        mers_answer,
        lambda call: call.data == "mers"
    )
    dp.register_callback_query_handler(
        bmw_answer,
        lambda call: call.data == "bmw"
    )
    dp.register_callback_query_handler(
        auto_start,
        lambda call: call.data == "auto"
    )
    dp.register_callback_query_handler(
        ios_answer,
        lambda call: call.data == "ios"
    )
    dp.register_callback_query_handler(
        android_answer,
        lambda call: call.data == "android"
    )
    dp.register_callback_query_handler(
        phone_start,
        lambda call: call.data == "phone"
    )