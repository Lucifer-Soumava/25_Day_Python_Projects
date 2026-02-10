# 1. Get the user input for the total bill amount
print('Welcome to Expense Splitter™!')
while True:
    total_bill: float = input('1. Enter the total bill you would like to split: ')
    if total_bill.isnumeric():
        total_bill = float(total_bill)
        break
    print('Please enter a numeric value as your amount')

# 2. Add the participants to the bill
people: list[str] = []
print('2. Add participants (press Enter on an empty line when finished):')
while True:
    input_name: str = input('Name: ').lower()
    if input_name.strip() == '':
        if len(people)!=0:
            break
        print('Please enter atleast one name to pay the bill')
        continue

    # Check for duplicate names
    if input_name in people:
        print('That name is already listed or invalid. Please add a different name.')
    else:    
        people.append(input_name)

# 3. Splitting the bill
print('3. Now, specify the percentage each person will pay.')
print('(Type "even" at any time to split the bill equally.)')

# Create a dictionary that holds how much each person owes
people_dict: dict[str, float] = {}
total_percent: float = 100.0

# Get inputs for each person
for person in people:
    while True:
        percent_input: str = input(f'[{total_percent:.0f}% remaining] {person.capitalize()}: ').lower()

        # If you tap on enter, 0 will be the default value
        if percent_input.strip() == '':
            percent_input = '0'

        # Typing 'even' will split the bill evenly
        if percent_input.strip() == 'even':
            for nested_person in people:
                people_dict[nested_person] = (1 / len(people)) * total_bill
            break

        # Must be a number
        if not percent_input.replace('.', '', 1).isdigit():
            print('Please enter a valid number, "even", or press Enter.')
            continue

        percent = float(percent_input)

        # Cannot exceed remaining percentage
        if percent > total_percent:
            print(f'You only have {total_percent:.0f}% remaining.')
            continue

        break  # valid input

    # Stop assigning if evenly split
    if percent_input == 'even':
        break

    people_dict[person] = (float(percent_input) / 100) * total_bill
    total_percent -= float(percent_input)

# 4. Display the information
print('\n--- Split Summary ---')
for name, share in people_dict.items():
    print(f'{name.capitalize():10}: ${share:,.2f}')
print('---------------------')
