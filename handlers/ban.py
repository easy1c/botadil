from aiogram import types, Dispatcher
from database import bot_db


async def check_ban(call: types.CallbackQuery):
    db = bot_db.Database()
    ban_user = db.sql_select_ban_user(tg_id=call.from_user.id)

    if ban_user:
        await call.message.answer(f"Вы находитесь в списке забаненных пользователей. "
                            f"Количество нарушений: {ban_user['count']}")
    else:
        await call.message.answer("Вы не нарушали правила и не находитесь в списке забаненных пользователей.")

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(check_ban,
        lambda call: call.data == "ban")

    "ebashim next"
