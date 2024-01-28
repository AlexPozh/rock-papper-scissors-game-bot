from config_data.config import GAME_STUFFS

from random import choice


def bot_move() -> str:
    """Functiot return the bot's move: Rock, Paper or Scissors"""
    return choice(GAME_STUFFS)