import json

def load_exchange_rates() -> dict[str, float]:
    with open('currencies.json', 'r') as file:
        return json.load(file)

def instructions() -> None:
    print('1. Type <amount><CURRENCY>, e.g. 10USD, to convert a currency.')
    print('2. Type LIST to list available currencies.')
    print('3. Type QUIT to exit.')

# --- NEW HOMEWORK FUNCTIONS ---

def get_conversions(user_input: str, rates: dict[str, float]) -> dict[str, float] | None:
    """Calculates all conversions and returns them as a dictionary."""
    currency_codes: list[str] = list(rates.keys())
    input_currency_code: str = user_input[-3:]

    # Validation
    if input_currency_code not in currency_codes:
        print(f'Currency code: "{input_currency_code}" is invalid.')
        return None

    try:
        input_amount: float = float(user_input[:-3])
    except ValueError:
        print(f'"{user_input}" is invalid. Try something like: "10 AUD"')
        return None

    # Base conversion (to USD)
    base_amount_usd: float = input_amount / rates[input_currency_code]

    # Create a dictionary of all possible conversions
    results = {}
    for code, rate in rates.items():
        results[code] = base_amount_usd * rate
    
    return results

def display_conversions(input_str: str, results: dict[str, float]) -> None:
    """Handles the visual formatting of the converted data."""
    input_currency = input_str[-3:]
    input_amount = float(input_str[:-3])

    print(f'{round(input_amount, 2):>16} {input_currency}')
    print('-' * 20)
    for code, amount in results.items():
        print(f'= {round(amount, 2):>14} {code}')
    print('-' * 20)

# --- UPDATED MAIN ---

def main() -> None:
    instructions()
    exchange_rates: dict[str, float] = load_exchange_rates()

    while True:
        user_input: str = input('Convert: ').upper().strip()

        if user_input == 'LIST':
            print(f'Available currencies: {", ".join(exchange_rates.keys())}')
            continue
        elif user_input == 'QUIT':
            print('Exiting.')
            break

        # Call the calculation function
        conversion_data = get_conversions(user_input, exchange_rates)
        
        # Only display if the calculation was successful (not None)
        if conversion_data:
            display_conversions(user_input, conversion_data)

if __name__ == '__main__':
    main()