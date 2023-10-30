def convert_length(value, from_unit, to_unit):
    if from_unit == "meters" and to_unit == "feet":
        return value * 3.28084
    elif from_unit == "feet" and to_unit == "meters":
        return value / 3.28084
    else:
        return None

def main():
    while True:  # Add a loop to allow for multiple conversions
        print("Welcome to the Length Converter!")

        try:
            value = float(input("Enter a value to convert: "))
            from_unit = input("Enter the source unit (meters/feet): ").lower()
            to_unit = input("Enter the target unit (meters/feet): ").lower()

            result = convert_length(value, from_unit, to_unit)
            if result is not None:
                print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
            else:
                print("Unsupported units. Please choose meters or feet.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion=="no":
            print("Thankyou")
        if another_conversion != "yes":
            break  # Exit the loop if the user does not want another conversion

if __name__ == "__main__":
    main()

