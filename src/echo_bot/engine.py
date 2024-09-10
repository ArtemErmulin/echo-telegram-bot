import asyncio
import logging

from telegram import Update
from telegram.ext import Application, Updater

from config import settings
from echo_bot.handlers import set_handlers
from echo_bot.webserver import set_up_webserver, set_webhook

logger = logging.getLogger(__name__)


def set_up_application(with_updater: bool) -> Application:
    """
    Set up the application.

    Parameters
    ----------
    with_updater : bool
        Whether to set up the updater or not.

    Returns
    -------
    Application
        The application instance.
    """
    application = (
        Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    )

    if with_updater:
        application.updater = Updater(
            bot=application.bot, update_queue=application.update_queue
        )

    set_handlers(application)

    return application


async def send_startup_message(application: Application):
    """
    Send a message to the admin chat (if 'ADMIN_CHAT_ID' available)
    when the bot is running.
    """
    # ADMIN_CHAT_ID is optional
    if not settings.ADMIN_CHAT_ID:
        return

    await application.bot.send_message(
        chat_id=settings.ADMIN_CHAT_ID,
        text="Bot is running.",
    )


async def async_run():
    """
    Run the bot using the webhook.
    """
    application = set_up_application(with_updater=False)
    webserver = set_up_webserver()

    await set_webhook(application)
    await send_startup_message(application)

    async with application:
        await application.start()
        await webserver.serve()
        await application.stop()


def run_polling():
    """
    Run the bot using polling.
    """
    application = set_up_application(with_updater=True)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_startup_message(application))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


def run():
    """
    Main function to run the bot.

    If the webhook is available, the bot will use the webhook.
    Otherwise, the bot will use polling.
    """
    if settings.WEBHOOK_URL:
        logger.info("Webhook is available. Webhook will be used.")
        asyncio.run(async_run())

    else:
        logger.info("Webhook is not available. Polling will be used.")
        run_polling()
