"""
You are given a non-negative floating point number rounded to two decimal places celsius, 
that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array 
ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.

Note that:

Kelvin = Celsius + 273.15
Fahrenheit = Celsius * 1.80 + 32.00
"""


def conv_c_to_k_and_f(celsius: float) -> list:
    """
    Convert Celsius to Kelvin and Fahrenheit
    """
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    ans = [kelvin, fahrenheit]
    return ans


def user_input_celsius():
    """
    Ask user to input correct number of celsius. Show error if input incorrect.
    """
    while True:
        try:
            celsius = float(input("\nPlease, write celsius: "))
            return celsius
        except ValueError:
            print("\nError. Please use one floating point or integer number")
            continue


next_c = "y"
while next_c == "y":
    print("\n[kelvin, fahrenheit]" +
          str(conv_c_to_k_and_f(user_input_celsius())))
    while True:
        next_c = input("\nNext? y/n : ")
        if next_c.lower() == "n" or next_c.lower() == "y":
            break
        else:
            print("\nError. Please use letters 'y' for yes and 'n' for no")
            continue
