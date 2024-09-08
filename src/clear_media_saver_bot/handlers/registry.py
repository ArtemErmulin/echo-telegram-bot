from telegram.ext import Application, CommandHandler, MessageHandler, filters

from .echo_handler import echo
from .start_handler import start

# All handlers must be imported and added to this list.
HANDLERS = [
    CommandHandler("start", start),
    MessageHandler(filters.TEXT & ~filters.COMMAND, echo),
]


def set_handlers(application: Application) -> None:
    for handler in HANDLERS:
        application.add_handler(handler)
