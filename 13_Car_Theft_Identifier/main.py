class Car:
    def __init__(self, liscence_plate: str) -> None:
        if len(liscence_plate) != 6:
            raise ValueError('Invalid liscence plate.')
    
        self.liscence_plate = liscence_plate.upper()

class StolenCarRegistry:
    def __init__(self):
        self.stoles_plates: set[str] = set()

    def add_stolen_plates(self, plates: list[str]) -> None:
        for plate in plates:
            self.stoles_plates.add(plate.upper())

    def is_stolen(self, plate: str) -> bool:    
        return plate.upper() in self.stoles_plates
    
    def remove_stolen(self, plate: str) -> None:
        plates = list(self.stoles_plates)
        if plate.upper() in plates:
            removed: str = plates.pop(plates.index(plate.upper()))
            print(f'The Car with {removed} plate no. has been found!')
            self.stoles_plates.remove(plate.upper())
        else:
            print('Removal cannot take place with a car that wasnt stolen!')
        

    def count_stolen(self) -> int:
        return len(self.stoles_plates)
    
    def display_plates(self) -> None:
        for plate in self.stoles_plates:
            print(plate)
    
def main() -> None:
    registry: StolenCarRegistry = StolenCarRegistry()
    registry.add_stolen_plates(['ABC123', 'XYZ999', 'BOB789'])

    print('Welcome to Car Theft Identifier')
    while True:
        plate: str = input('Enter car liscence plate: ').strip()
        car: Car = Car(plate)

        if registry.is_stolen(car.liscence_plate):
            print(f'❌ Car with plate "{car.liscence_plate}" is: REPORTED STOLEN!')
        else:
            print(f'✅ Car with plate "{car.liscence_plate}" is: OK')
        break
    registry.display_plates()
    print(registry.count_stolen())
    registry.remove_stolen(plate)
    registry.display_plates()
    print(registry.count_stolen())

if __name__ == '__main__':
    main()