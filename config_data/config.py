from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Telegram API bot token


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    """
    Reads environment variables from .env and returns an
    instance of a class Config.

    :param path: path to .env
    """
    # Создаем экземпляр класса Env
    env = Env()
    # Добавляем в переменные окружения данные, прочитанные из файла .env
    env.read_env(path)
    # Возвращаем экземпляр класса Config и наполняем его данными из переменных
    # окружения
    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN")
        )
    )


if __name__ == "__main__":
    print(load_config("../.env"))
