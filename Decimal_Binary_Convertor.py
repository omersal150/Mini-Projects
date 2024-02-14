print("Welcome to Decimal to Binary Converter")
print("Made by the mighty Omer Salamander")

decimal = int(input("Please provide a Decimal number to convert: "))
answer = decimal
binary = []

while decimal > 0:
    remainder = decimal % 2
    binary.insert(0, remainder)
    decimal = decimal // 2

binary_str = ''.join(map(str, binary))

print("Thats a good one let me think")
print("The Binary equivalent for the number", answer, "is :", binary_str)
