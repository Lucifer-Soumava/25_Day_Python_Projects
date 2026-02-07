# Get user input and calculate tax
base_income: float = float(input('Enter your yearly income: '))
tax_rate: float = float(input('Enter your tax rate percentage: ')) / 100
taxed: float = base_income * tax_rate
doubled_income: float = base_income * 2
tripled_income: float = base_income * 3
taxed_doubled: float = doubled_income * tax_rate
taxed_tripled: float = tripled_income * tax_rate

# Display the data
print('=' * 40)
print('Income Tax Calculator')
print('=' * 40)
print(f'Base Income:              ${base_income:,.2f}')
print(f'Base Income (Doubled):    ${doubled_income:,.2f}')
print(f'Base Income (Tripled):    ${tripled_income:,.2f}')
print(f'Tax Rate:                 {tax_rate:.0%}')
print('-' * 40)
print(f'Yearly Tax (Base):        ${taxed:,.2f}')
print(f'Yearly Tax (Doubled):     ${taxed_doubled:,.2f}')
print(f'Yearly Tax (Tripled):     ${taxed_tripled:,.2f}')
print('=' * 40)
