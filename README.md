# Simple Echo Telegram Bot
<p align="center">
    <img src="https://img.shields.io/badge/license-MIT-green.svg">
    <img src="https://img.shields.io/badge/config-dynaconf-blue">
</p>


---

A simple echo Telegram bot template built using Docker and managed through Coolify. This bot can be used as a starting point for developing your own Telegram bots.


## Features

- Echoes back the messages it receives.
- Easily deployable on any server or virtual machine.
- Managed via [Coolify](https://coolify.io/), allowing for continuous deployment and webhook handling.
- Includes customizable environment variables for easy configuration.

## Requirements

- Docker installed on the target server/VM.
- Coolify for managing the deployment (can be installed on the same or a separate server).
- A GitHub repository where the bot's code is stored.

## Deployment

### 1. Coolify Setup

You can find instructions for installing and deploying Coolify on its [official website](https://coolify.io/). Once installed:

- Link your GitHub account so Coolify can access your repositories.
- Create a new application in Coolify and link it to your bot's repository.

### 2. Bot Application Setup in Coolify

To correctly set up the bot in Coolify, follow these steps:

1. Set `Build Pack` to `Dockerfile`.
2. In `Domains`, replace the suggested `http://` with `https://`. This is required for the webhook to function correctly.
3. In `Network`, under `Ports Exposes`, specify port `8443`.
4. In `Environment Variables`, configure the following variables for the bot (see below).
5. Enable `Health Check` and specify the `Host` and `Port` (defaults are `0.0.0.0` and `8443`).

### 3. Environment Variables

The bot requires the following environment variables:

- `ETB_TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `ETB_WEBHOOK_URL`: The full webhook URL, including `https://`.
- `ETB_PORT`: (Optional) The port the bot will use, default is `8443`.
- `ETB_ADMIN_CHAT_ID`: (Optional) Admin chat ID for sending bot status messages.

> **Note:** `ETB_` is the prefix used with the `dynaconf` library (see `config.py` for more details).

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/echo-telegram-bot.git
   cd echo-telegram-bot

2. Build and run the Docker container:
    ```bash
    docker-compose up --build -d
    ```

3. Configure your environment variables in Coolify as mentioned above.

4. Deploy the bot and ensure it's running by checking the webhook in Telegram.

## Contributing

Feel free to fork this repository and contribute to it. Any improvements to the template or suggestions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

