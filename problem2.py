"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)



def fahrenheit_to_celsius(fahrenheit):
    """Convert a Fahrenheit temperature to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)



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
    try:
        #get temperature value
        temp = float(input("Enter temperature value:"))
        unit = input("Is this in Celsius (C) or Fahrenheit (F)? ").strip().upper()

        if unit == "C":
            converted = celsius_to_fahrenheit(temp)
            print(f"{temp:.2f}°C is {converted:.2f}°F")
        elif unit == "F":
            converted = fahrenheit_to_celsius(temp)
            print(f"{temp:.2f}°F is {converted:.2f}°C")
        else:
            print("Invalid unit. Please enter C or F.")
    except ValueError:
        print("Invalid input. Please enter a number.")




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
