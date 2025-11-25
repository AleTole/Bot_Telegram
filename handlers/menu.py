from telegram import Update
from telegram.ext import ContextTypes

async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # evita que Telegram quede cargando

    data = query.data

    if data == "registro":
        await query.edit_message_text(
            "🔗 Para registrarte llena este formulario:\n👉 https://forms.gle/hd5Dx8apjQRekNRb6"
        )

    elif data == "rrss":
        await query.edit_message_text(
            "🎥 Para conectarte a los en vivos entra a:\nYouTube: @CreeemosCapital\nTikTok: @CreeemosCapital"
        )
    
