import random
import sys
import time

class SlotMachine:
    def __init__(self, credits: int) -> None:
        self.credits = credits
        self.symbols: dict[str, int] = {'🍒': 1, '🍇': 2, '🍊': 3, '🍋': 5}

    def spin(self, bet: int) -> None:
        if bet <= 0:
            print('Bet must be greater than 0...')
            return
        
        if self.credits >= bet:
            self.update_credits(-bet)
        else:
            print('Not enough credits...')
            return
        
        result: list[str] = []
        for _ in range(3):
            time.sleep(0.2)
            landed: str = random.choice(list(self.symbols))
            print(landed, end='', flush=True)
            result.append(landed)

        print()
        
        winnings: int = self.calculate_winnings(result, bet)
        if winnings != 0:
            print(f'Credits won: {winnings}')
            self.credits += winnings
        else:
            partial: int = self.calculate_partial(result, bet)
            print(f'Credits won {partial}')
            self.credits += partial
        
        if self.credits == 0:
            print('Game Over!')
            sys.exit()
        else:
            print(f'Credits remaining: {self.credits}')
            print('-' * 30)

    def calculate_partial(self, result: list[str], bet: int) -> int:
        previous: str = result[0]
        winnings: list[int] = []

        for symbol in range(2):
            if result[symbol] == previous:
                winnings.append(self.symbols[result[symbol]])
            else:
                winnings.clear()
                break

        return (sum(winnings)//2) * bet

    def calculate_winnings(self, result: list[str], bet: int) -> int:
        previous: str = result[0]
        winnings: list[int] = []

        for symbol in result:
            if symbol == previous:
                winnings.append(self.symbols[symbol])
            else:
                winnings.clear()
                break

        return sum(winnings) * bet


    def update_credits(self, amount: int) -> None:
        self.credits += amount

    def play(self) -> None:
        print(f'Starting credits: {self.credits}')
        print('-' * 30)
        while True:
            try:
                bet: int = int(input('Bet: '))
                self.spin(bet)
            except ValueError:
                print('Enter a valid number...')

def main() -> None:
    pokies: SlotMachine = SlotMachine(200)
    pokies.play()

if __name__ == '__main__':
    main()
