#menu_callbacks.py
from telegram import Update
from telegram.ext import ContextTypes
from keyboards.menu import main_menu, back_button
from texts.messages import (
    TEXTO_REGISTRO,
    TEXTO_RRSS,
    WELCOME_MSG
)

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    # 📋 REGISTRO
    if data == "registro":
        await query.edit_message_text(
            TEXTO_REGISTRO,
            reply_markup=back_button(),
            parse_mode="Markdown"
        )

    # 🎥 RRSSS
    elif data == "rrss":
        await query.edit_message_text(
            TEXTO_RRSS,
            reply_markup=back_button(),
            parse_mode="Markdown"
        )

    # ⬅️ VOLVER AL MENÚ
    elif data == "back_to_menu":
        await query.edit_message_text(
            WELCOME_MSG,
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )
