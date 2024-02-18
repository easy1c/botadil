
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire",
        callback_data="start_questionnaire"
    )
    choice_button = InlineKeyboardMarkup(
        text = "Choice",
        callback_data="choice"
    )
    auto_button = InlineKeyboardMarkup(
        text="Auto",
        callback_data="auto"
    )
    phone_button = InlineKeyboardMarkup(
        text="Phone",
        callback_data="phone"
    )

    markup.add(questionnaire_button)
    markup.add(choice_button)
    markup.add(auto_button)
    markup.add(phone_button)
    return markup
