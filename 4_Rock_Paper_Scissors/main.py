import random

# Choices available
choices = {
    'Rock':'🪨',
    'Paper':'📄',
    'Scissors':'✂️'
}

# User Inputs

players_choice = input("Choose rock (🪨 ), paper (📄 ), or scissors (✂️ ): ").strip().capitalize()
computer_choice = random.choice(tuple(choices))

# Results Showcase

print('Results')
print('--------------------------')
print(f'You :     {choices[players_choice]}  {players_choice}')
print(f'Computer :     {choices[computer_choice]}  {computer_choice}')
print('--------------------------')

# Winning side choosing

if players_choice == 'Rock' and computer_choice == 'Scissors':
    print("Player wins")
elif players_choice == 'Paper' and computer_choice == 'Rock':
    print("Players wins")
elif players_choice == 'Scissors' and computer_choice == 'Paper':
    print("Players wins")
else:
    print("Player loses")