"""Temperature conversions."""


def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: The temperature in degrees Celsius.

    Returns:
        The equivalent temperature in degrees Fahrenheit.
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    # Wrong: the 32-degree offset is missing.
    return fahrenheit * 5 / 9
