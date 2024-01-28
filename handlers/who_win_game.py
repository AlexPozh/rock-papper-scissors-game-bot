from config_data.config import GAME_STUFFS


def who_win(user_stuff: str, bot_stuff: str) -> str:
    """This function defines the result of the move in the game: Draw, lose, win"""

    # Check draw
    if user_stuff == bot_stuff:
        return "Draw!"
    
    # Define the winner and the loser
    match user_stuff.lower():
        case "rock":
            if bot_stuff.lower() == "scissors":
                return "You win!"
            else:
                return "You lose!"

        case "paper":
            if bot_stuff.lower() == "rock":
                return "You win!"
            else:
                return "You lose!"

        case "scissors":
            if bot_stuff.lower() == "paper":
                return "You win!"
            else:
                return "You lose!"


def define_result(user_stuff: str, bot_stuff: str) -> str:
    """This function returns the result after the move in the game"""

    # Check the correct answer from the user
    if user_stuff not in GAME_STUFFS:
        return f"Please, write the correct stuffs, like Rock, Paper, Scissors"
    
    return who_win(user_stuff, bot_stuff)
