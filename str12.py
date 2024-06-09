def is_multiple_of_3(binary_string):
    return int(binary_string, 2) % 3 == 0
binary_input = input("Enter a binary string:")
if(binary_input):
    print("The binary string is a multiple of 3,")
else:
    print("The binary string is not a multiple of 3,")
