from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def python_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Python🐍",
        callback_data="python"
    )
    mojo_button = InlineKeyboardButton(
        "Mojo🫀",
        callback_data="mojo"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def dota_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    dota_button = InlineKeyboardButton(
        "Dota2",
        callback_data="dota"
    )
    LOL_button = InlineKeyboardButton(
        "LOL",
        callback_data="LOL"
    )
    markup.add(dota_button)
    markup.add(LOL_button)
    return markup


async def auto_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    mers_button = InlineKeyboardButton(
        "Mercedes Benz",
        callback_data="mers"
    )
    bmw_button = InlineKeyboardButton(
        "BMW",
        callback_data="bmw"
    )
    markup.add(mers_button)
    markup.add(bmw_button)
    return markup

async def phone_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    ios_button = InlineKeyboardButton(
        "IOS",
        callback_data="ios"
    )
    android_button = InlineKeyboardButton(
        "Android",
        callback_data="android"
    )
    markup.add(ios_button)
    markup.add(android_button)
    return markup


async def pythonp_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_python"
    )
    python_no_button = InlineKeyboardButton(
        "No",
        callback_data="no_python"
    )
    markup.add(python_button)
    markup.add(python_no_button)
    return markup