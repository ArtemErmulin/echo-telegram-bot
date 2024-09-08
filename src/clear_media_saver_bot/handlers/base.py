from functools import wraps
from typing import Any, Callable, Coroutine, cast

from telegram import Message, Update
from telegram.ext import CallbackContext

HandlerReturnType = Coroutine[Any, Any, None]
HandlerFuncType = Callable[[Update, CallbackContext], HandlerReturnType]


# Only for type hinting
class UpdateNotEmptyMessage(Update):
    message: Message


def check_empty_message(func) -> HandlerFuncType:
    """
    Decorator for handlers that checks if the update has a message.
    """

    @wraps(func)
    async def wrapper(update: Update, context: CallbackContext):
        if update.message is not None:
            update = cast(UpdateNotEmptyMessage, update)
            return await func(update, context)

    return wrapper
