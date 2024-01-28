from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove

from aiogram.filters import Command, CommandStart

from aiogram import Router, F

from lexicon.lexicon import LEXICON_RU, LEXICON_ENG

from aiogram.utils.keyboard import ReplyKeyboardBuilder

from .player_handlers import game_command

router: Router = Router()

# kb_builder = ReplyKeyboardBuilder()

# buttons: list[KeyboardButton] = [
#     KeyboardButton(text = "/game"),
# ]

# kb_builder.row(*buttons)

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(LEXICON_ENG["/start"])


@router.message(Command(commands="help"))
async def help_command(message: Message):
    await message.answer(LEXICON_ENG["/help"])

# @router.message(F.text.in_(["You win!", "Draw!", "You lose!"]))
# async def show_result(message: Message):





