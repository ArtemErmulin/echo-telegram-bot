from telegram.ext import CallbackContext

from clear_media_saver_bot.handlers.base import (
    UpdateNotEmptyMessage,
    check_empty_message,
)


@check_empty_message
async def start(update: UpdateNotEmptyMessage, context: CallbackContext):
    await update.message.reply_html("Hello! I'm a simple echo bot!")
