def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

def main():
    print("Welcome to Decimal-Binary Converter")
    print("Made By Omer Salamander")

    while True:
        conversion_type = input("Choose conversion type:\n1. Decimal to Binary\n2. Binary to Decimal\n3. Exit\nEnter your choice: ")

        if conversion_type == '1':
            decimal_input = int(input("Enter a decimal number: "))
            print("Binary equivalent:", decimal_to_binary(decimal_input))

        elif conversion_type == '2':
            binary_input = input("Enter a binary number: ")
            print("Decimal equivalent:", binary_to_decimal(binary_input))

        elif conversion_type == '3':
            print("Exiting the converter. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
