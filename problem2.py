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

    try:
        temperature_input = float(input("Please type the temperature that you would like to convert as a numerical value: "))

    except ValueError:
        print("Please try again by inserting a numerical value")

    temperature_unit = input("Please type temperature measurement unit (C) or (F): ")
    if temperature_unit == "C":
            conversion = celsius_to_fahrenheit(temperature_input)
            print(f"{temperature_input:.2f}", " is equivalent to ", f"{conversion:.2f}", " degrees Fahrenheit")    

    elif temperature_unit == "F":
            conversion = fahrenheit_to_celsius(temperature_input)
            print(f"{temperature_input:.2f}", " is equivalent to ", f"{conversion:.2f}", " degrees Celsius")

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