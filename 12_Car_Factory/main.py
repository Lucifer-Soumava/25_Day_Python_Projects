from collections import Counter
from time import sleep
account = 0

class Car:
    def __init__(self, brand: str, color: str, model: int) -> None:
        self.brand = brand.capitalize()
        self.color = color.capitalize()
        self.model = model

    def drive(self, distance: int, speed: int) -> None:
        print(f'{self.brand} {self.model} [{self.color}] started journey...')
        for i in range(1, distance+1):
            sleep(60/speed)
            print(f'KM: {i}')
        
        print(f'{self.brand} {self.model} [{self.color}] completed journey...')

class Account:
    def __init__(self):
        self.balance = 0
    
    def debit(self, amount: int) -> None:
        self.balance += amount

def test_car() -> None:
    volvo: Car = Car('volvo', 'red', 200)
    volvo.drive(10, 140)

def create_cars(cars: list[Car]) -> None:
    brand: str = input('Enter the brand: ')
    color: str = input('Enter the color: ')
    try:
        model: int = int(input('Enter the model number: '))
        amount: int = int(input('Enter the amount: '))

        for i in range(amount):
            cars.append(Car(brand, color, model))
        
        print('Cars created!')
    except ValueError:
        print('Error creating the Car')

def display_stocks(cars: list[Car]) -> None:
    car_tuples: list[tuple[str, str, int]] = [(car.brand, car.color, car.model) for car in cars]
    counter: Counter[tuple[str, str, int]] = Counter(car_tuples)

    for (brand, color, model), count in counter.items():
        print(f'{brand} {model} [{color}]: {count} in stock')


def sell(cars: list[Car], acc: Account ) -> None:
    car_tuples: list[tuple[str, str, int]] = [(car.brand, car.color, car.model) for car in cars]
    counter: Counter[tuple[str, str, int]] = Counter(car_tuples)

    brand = input("Enter brand: ").capitalize().strip()
    color = input("Enter color: ").capitalize().strip()
    model = int(input("Enter model number: "))

    key = (brand, color, model)

    if counter[key] == 0:
        print("Car not available")
    else:
        try:
            qty = int(input("How many do you want to sell? "))

            if qty > counter[key]:
                print(f"Only {counter[key]} available")
            else:
                counter[key] -= qty
                sp: int = int(input('Enter the amount you sold the car at: '))
                
                amount = sp * qty
                acc.debit(amount)
                print('Successfully debited to your account! ')
                print(f"Sold {qty} cars")

                if counter[key] == 0:
                    del counter[key]
        except ValueError:
                    print('Enter a correct numeric value')


def main() -> None:
    cars: list[Car] = [Car('volvo', 'red', 200),
                       Car('toyota', 'green', 500),
                       Car('porsche', 'yellow', 239)]
    
    acc = Account()
    
    print('Type: "create" to create cars and "display" to display current stock \n      "sell" to sell from the stock of cars "acc" to see account balance \n      "exit" to exit')
    while True:
        user_input: str = input('You: ').lower().strip()

        if user_input == 'create':
            create_cars(cars)
        elif user_input == 'display':
            display_stocks(cars)
        elif user_input == 'sell':
            sell(cars, acc)
        elif user_input == 'acc':
            print(f'You have ${acc.balance} in the account')
        elif user_input == 'exit':
            break
        else:
            print(f'Unknown command: "{user_input}"')

if __name__ == '__main__':
    main()