from dynaconf import Dynaconf, Validator

# ETB - Echo Telegram Bot
settings = Dynaconf(
    environments=True,
    envvar_prefix="ETB",
    settings_files=["settings.toml", ".secrets.toml"],
    validators=[
        Validator("TELEGRAM_BOT_TOKEN", is_type_of=str, must_exist=True),
        Validator("HOST", is_type_of=str, must_exist=True),

        # Optional
        Validator("ADMIN_CHAT_ID", is_type_of=int),
        Validator("WEBHOOK_URL", is_type_of=str),
        Validator("PORT", is_type_of=int, default=8443),
    ]
)
