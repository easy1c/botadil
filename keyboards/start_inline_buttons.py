
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire🫥",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration👾",
        callback_data="registration"
    )
    my_profile_button = InlineKeyboardButton(
        "My Profile🔥",
        callback_data="my_profile"
    )
    choice_button = InlineKeyboardMarkup(
        text = "Choice🫶",
        callback_data="choice"
    )
    auto_button = InlineKeyboardMarkup(
        text="Auto🛞",
        callback_data="auto"
    )
    phone_button = InlineKeyboardMarkup(
        text="Phone📱",
        callback_data="phone"
    )
    ban_button = InlineKeyboardMarkup(
        text="Ban⛔️",
        callback_data="ban"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(choice_button)
    markup.add(auto_button)
    markup.add(phone_button)
    markup.add(ban_button)
    markup.add(my_profile_button)
    return markup
