# Simple echo telegram bot
A simple echo Telegram bot to use as a template.


# Requirements
The bot's architecture assumes deployment on a dedicated server (or virtual machine) in a Docker container. The bot's deployment is managed via Coolify (which can be located on another server or on the same one).

## Coolify
The installation and deployment guide for Coolify can be found on the [official website](https://coolify.io/).  
After installation, you need to link a GitHub account so that Coolify can pull repositories.  
Next, create an project and specify the repository with the bot.


## Setting up the bot project in Coolify
1. Change `Build Pack` to `Dockerfile`;
2. Change `Domains`: switch to `https://` instead of suggested `http://`. This is required for correct webhook operation.
3. In `Network`, `Ports Exposes` specify port 8443.
4. In `Environment Variables`, set the environment variables for the bot.
5. Enable `Health Check` and specify `Host` and `Port` (default `0.0.0.0` и `8443`).

Once these steps are complete, the bot application setup in Coolify is finished.

## Environment variables
1. `ETB_TELEGRAM_BOT_TOKEN`
2. `ETB_WEBHOOK_URL`
3. `ETB_PORT` (optional, default 8443)
4. `ETB_ADMIN_CHAT_ID` (optional, for sending bot status)
Where `ETB_` is a prefix for the `dynaconf` library (see `config.py`).
