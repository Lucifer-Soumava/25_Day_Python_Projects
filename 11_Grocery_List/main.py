from json.tool import main


db: dict[str, int] = dict()

def announcement(msg: str) -> None: # Just an print type statement for different types of messages
    print(f'System: {msg}')

def add_item() -> None: # Adds Items to the list of items
    name: str = input('Enter an item: ').lower().strip()

    while True:
        try:
            quantity: int = int(input('Enter a quantity: '))

            if quantity <=0 :
                raise ValueError

            break # Exits the loop when quantity doesnt cause an error

        except ValueError:
            announcement('Error please enter a valid quantity')

    db[name] = quantity
    announcement(f'Added "{name}" x {quantity}')

def remove_item() -> None: # Removes the an item from the list
    name: str = input('Enter an item: ').lower().strip()

    try: 
        db.pop(name)
        announcement(f'Successfully removed {name}')

    except KeyError:
        announcement(f'{name} not found in the Grocery List.')

def view_list() -> None: # Shows the list of items
    if db:
        print('-'*20)
        for k, v in db.items():
            print(f'{k.capitalize():>15}{v}')
        print('-'*20)
    else:
        announcement('There are no items on the Grocery List.')

def modify_item() -> None: # Modifies the list if we need a new quantity
    if not db:
        announcement('There are no items on the Grocery List to modify.')
        return
    
    name: str = input('Enter the name of the item: ').lower().strip()

    if name not in db:
        announcement(f'{name} not present in your Grocery List.')
        return 
    
    while True:    
        try:
            quantity_new: int = int(input('Enter the actual value you want:'))
            
            if quantity_new <=0 :
                raise ValueError
            
            break
        except ValueError:
            announcement('Enter a valid number to modify')

    db[name] = quantity_new
    announcement(f'Updated {name} to {quantity_new}')

def display_options() -> None: # Shows the available options
    print('Options:')
    print('0 - Display options')
    print('1 - Read list')
    print('2 - Add to list')
    print('3 - Remove from list')
    print('4 - Modify items in the list')
    print('-')

def get_option(option: str) -> None:
    try: 
        converted: int = int(option)
    except ValueError:
        announcement('Error, please enter a valid option')
        return
    
    if converted == 0:
        display_options()
    elif converted == 1:
        view_list()
    elif converted == 2:
        add_item()
    elif converted == 3:
        remove_item()
    elif converted == 4:
        modify_item()
    else:
      announcement('Enter a number within the options')  

def main() -> None:

    display_options()
    
    while True:
        user_input: str = input('You')
        get_option(user_input)
    
if __name__ == "__main__":
    main()
