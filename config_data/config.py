from environs import Env

from dataclasses import dataclass

from typing import TypeAlias

BotToken: TypeAlias = str

GAME_STUFFS = ["Rock", "Paper", "Scissors"]

@dataclass()
class TelegramBot:
    token_bot: BotToken


@dataclass()
class Config:
    tg_bot: TelegramBot


def get_config(path: str | None) -> Config:
    env: Env = Env()

    env.read_env()

    return Config(tg_bot=TelegramBot(token_bot = env("BOT_TOKEN")))
