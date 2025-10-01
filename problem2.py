"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    return((celsius * 9/5) + 32)

def fahrenheit_to_celsius(fahrenheit):
    return((fahrenheit - 32) * 5/9)

def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    # TODO: Implement the interactive converter
    # Remember to:
    # - Get temperature value from user
    # - Get unit (C or F) from user
    # - Validate input
    # - Perform conversion
    # - Display result rounded to 2 decimal places

def celsius_to_fahrenheit(celsius):
    return((celsius * 9/5) + 32)

def fahrenheit_to_celsius(fahrenheit):
    return((fahrenheit - 32) * 5/9)

while  True:
    temperature_input = input("Enter the current temperature (C for Celsius, F for Fahrenheit) ")

    if temperature_input == "C":
        c = float(input("Please type the temperature that you would like to convert as a numerical value "))
        celsius_to_fahrenheit(c)
        print(c, " is equivalent to ", celsius_to_fahrenheit, " degrees Fahrenheit")
        break

    elif temperature_input == "F":
        f = float(input("Please type the temperature that you would like to convert as a numerical value "))
        fahrenheit_to_celsius(f)
        print(f, " is equivalent to ", fahrenheit_to_celsius, " degrees Celsius")
        break

    else:
        print("Please try again by inserting C or F")

# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()