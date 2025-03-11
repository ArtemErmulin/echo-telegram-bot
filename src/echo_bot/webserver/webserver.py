from http import HTTPStatus

import uvicorn
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, Response, request
from telegram import Update
from telegram.ext import Application

import config

flask_app = Flask(__name__)


def set_up_webserver() -> uvicorn.Server:
    webserver = uvicorn.Server(
        config=uvicorn.Config(
            app=WsgiToAsgi(flask_app),
            host=config.HOST,
            port=config.PORT,
            use_colors=False,
        ),
    )

    return webserver


async def set_webhook(application: Application) -> None:
    @flask_app.post("/telegram")
    async def _() -> Response:
        await application.update_queue.put(
            Update.de_json(
                data=request.json,
                bot=application.bot,
            )
        )

        return Response(status=HTTPStatus.OK)

    await application.bot.set_webhook(
        url=f"{config.WEBHOOK_URL}/telegram",
        allowed_updates=Update.ALL_TYPES,
    )
