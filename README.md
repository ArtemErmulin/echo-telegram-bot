# Simple Echo Telegram Bot
<p align="center">
    <img src="https://img.shields.io/badge/license-MIT-green.svg">
    <img src="https://img.shields.io/badge/config-dynaconf-blue">
</p>


---

A simple echo Telegram bot template built using Docker. This bot can be used as a starting point for developing your own Telegram bots.

> ⚠️ The template is still under development

## Features

- Echoes back the messages it receives.
- Easily deployable on any server or virtual machine.
- Includes customizable environment variables for easy configuration.

## Requirements

- Docker installed on the target server/VM.
- A GitHub repository where the bot's code is stored.

## Deployment

The bot requires the following environment variables:

- `ETB_TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `ETB_WEBHOOK_URL`: The full webhook URL, including `https://`.
- `ETB_PORT`: (Optional) The port the bot will use, default is `8443`.
- `ETB_ADMIN_CHAT_ID`: (Optional) Admin chat ID for sending bot status messages.

> **Note:** `ETB_` is the prefix used with the `dynaconf` library (see `config.py` for more details).

These environment variables can be set in the `.secrets.toml` file.

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/ArtemErmulin/echo-telegram-bot.git
   cd echo-telegram-bot

1. Create a `.secrets.toml` file from `.secrets_example.toml` in the root directory and add the required environment variables.

1. Build and run the Docker container:
    ```bash
    docker-compose up --build -d
    ```
> **Note:** When running locally (if the `WEBHOOK_URL` environment variable is not set), the bot will start in polling mode.


## Contributing

Feel free to fork this repository and contribute to it. Any improvements to the template or suggestions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

