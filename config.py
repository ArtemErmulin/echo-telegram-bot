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


def get_int(key: str) -> int:
    try:
        raw_value = getattr(settings, key)
        value: int = int(raw_value)

    except ValueError:
        raise ValueError(f"{key} must be an integer, but got '{raw_value}'.")
    return value


def get_str(key: str) -> str:
    return str(getattr(settings, key))



HOST: str = get_str("HOST")
PORT: int = get_int("PORT")
TELEGRAM_BOT_TOKEN: str = get_str("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID: int = get_int("ADMIN_CHAT_ID")
WEBHOOK_URL: str = get_str("WEBHOOK_URL")
