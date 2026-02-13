from typing import Final
import random

LOWER_LIMIT: Final[int] = 0
UPPER_lIMIT: Final[int] = 100
random_number: int = random.randint(LOWER_LIMIT, UPPER_lIMIT)

def bot_message(msg: str) -> None:
    print(f'Bot: {msg}')

bot_message('Welcome to GuessTheNumber')
bot_message(f'Guess the number between {LOWER_LIMIT} & {UPPER_lIMIT}')
tries: int = 0
while True:
    try:
        user_guess: int = int(input('You: '))
        tries += 1
    except ValueError as e:
        bot_message(f'{e}, please only use numbers.')
        continue

    if user_guess > random_number:
        bot_message('The number is lower.')
    elif user_guess < random_number:
        bot_message('The number is higher.')
    else:
        bot_message(f'You guessed correctly in {tries} tries! You win!')
        break
