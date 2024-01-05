def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    print("Select an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice not in [1, 2]:
            print("Invalid choice. Please enter 1 or 2.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if choice == 1:
        try:
            celsius = float(input("Enter the temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        try:
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    temperature_converter()
