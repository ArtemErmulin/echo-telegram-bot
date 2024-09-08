from typing import Optional

from telegram import Update
from telegram.ext import CallbackContext

from echo_bot.handlers.base import HandlerReturnType


async def echo(
    update: Update, _: CallbackContext
) -> Optional[HandlerReturnType]:
    """
    Echo handler that sends the received text back to the chat.
    """
    if update.message:
        await update.message.reply_text(update.message.text or "No text found")

    return None
