from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    keyboard = [
        [InlineKeyboardButton("📋 ¿Cómo me registro?", callback_data="registro")],
        [InlineKeyboardButton("🎥 ¡Siguenos y no te pierdas de nada!", callback_data="rrss")],
    ]
    return InlineKeyboardMarkup(keyboard)

def back_button():
    keyboard = [
        [InlineKeyboardButton("⬅️ Volver al menú", callback_data="back_to_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)
