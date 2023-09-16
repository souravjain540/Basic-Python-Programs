def encode(message, shift_value):
    message_letter_list = []
    for i in range(0, len(message)):
        message_letter_list.append(ord(message[i]))
        element_ascii = message_letter_list[i]
        new_ascii = element_ascii + shift_value
        if 97 <= message_letter_list[i] <= 122:
            while new_ascii > 122:
                new_ascii = element_ascii + shift_value - 123 + 97
            message_letter_list[i] = new_ascii
            # else:
            #     message_letter_list[i] = new_ascii
        elif 65 <= message_letter_list[i] <= 90:
            while new_ascii > 90:
                new_ascii = element_ascii + shift_value - 91 + 65
            message_letter_list[i] = new_ascii
        else:
            pass
    new_message = ""
    for element in message_letter_list:
        new_message += chr(element)
    print(new_message)


def decode(message, shift_value):
    message_letter_list = []
    for i in range(0, len(message)):
        message_letter_list.append(ord(message[i]))
        element_ascii = message_letter_list[i]
        new_ascii = element_ascii - shift_value
        if 97 <= message_letter_list[i] <= 122:
            while new_ascii < 97:
                new_ascii = element_ascii - shift_value + 123 - 97
            message_letter_list[i] = new_ascii
            # else:
            #     message_letter_list[i] = new_ascii
        elif 65 <= message_letter_list[i] <= 90:
            while new_ascii < 65:
                new_ascii = element_ascii - shift_value + 91 - 65
            message_letter_list[i] = new_ascii
        else:
            pass
    new_message = ""
    for element in message_letter_list:
        new_message += chr(element)
    print(new_message)


print("Welcome to caeser cipher program.")
command = input("Type e for encode and d for decode: ").lower()
if command == "e":
    message = input("Enter the message to encode: ")
    shift_value = int(input("Enter the shift value: "))
    encode(message, shift_value)
elif command == "d":
    message = input("Enter the message to decode: ")
    shift_value = int(input("Enter the shift value: "))
    decode(message, shift_value)
