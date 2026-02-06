# Constants
MILES_TO_KILOMETER = 1.609344
KILOMETER_TO_MILES = 0.6213712

# User Input
miles_input = 15.4
kilometer_input = 20.3

# Conversion
kilometer_converted = miles_input * MILES_TO_KILOMETER
miles_converted = kilometer_input * KILOMETER_TO_MILES

print(f"{miles_input}mi -> {kilometer_converted:.2f}km")
print(f"{kilometer_input}km -> {miles_converted:.2f}mi")