from telegram import Update
from telegram.ext import ContextTypes
from keyboards.menu import main_menu
from texts.messages import WELCOME_MSG
from config import WHITELIST, ENABLE_WHITELIST

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # If whitelist is enabled and user is not in it, ignore
    if ENABLE_WHITELIST and WHITELIST is not None and user_id not in WHITELIST:
        return  # ignoramos usuarios no autorizados

    await update.message.reply_text(
        WELCOME_MSG,
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )
