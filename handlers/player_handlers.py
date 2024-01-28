from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove

from aiogram.filters import Command, CommandStart

from aiogram import Router, F

from aiogram.utils.keyboard import ReplyKeyboardBuilder

from .game_timer import game_timer

from .bot_stuff import bot_move

from .who_win_game import define_result

router: Router = Router()

# ------------------------------------------------------
kb_builder = ReplyKeyboardBuilder()

buttons: list[KeyboardButton] = [
    KeyboardButton(text = "Rock"),
    KeyboardButton(text = "Paper"),
    KeyboardButton(text = "Scissors")
]

kb_builder.row(*buttons)

# ------------------------------------------------------
kb_builder_game = ReplyKeyboardBuilder()

button_game: list[KeyboardButton] = [
    KeyboardButton(text = "/game"),
]

kb_builder_game.row(*button_game)
# ------------------------------------------------------


@router.message(Command(commands="game"))
async def game_command(message: Message):

    # We wait for 3 seconds
    for sec in range(3, 0, -1):
        await message.answer(text = f"{sec}...")
        game_timer()

    await message.answer(
        text = "Choose the stuff:",
        reply_markup = kb_builder.as_markup(resize_keyboard=True)
        )


@router.message(F.text.in_(["Paper", "Rock", "Scissors"]))
async def player_move(message: Message):
    # generate the bot's move
    bot_step = bot_move()

    # calls function to define the result of the game
    game_result = define_result(message.text, bot_step)

    await message.answer(
        text = bot_step
        )
    
    await message.answer(
        text = game_result
        )
    
    match game_result:
        case "You win!":
            await message.answer(
                text = "Click the button below to restart a game.",
                reply_markup = kb_builder_game.as_markup(resize_keyboard = True))
            
        case "Draw!":
            await game_command(message)

        case "You lose!":
            await message.answer(
                text = "Click the button below to restart a game.",
                reply_markup = kb_builder_game.as_markup(resize_keyboard = True))
                






