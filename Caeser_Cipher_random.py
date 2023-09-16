import random
import os
def encode(message):
    message_letter_list = []
    decode_key = []
    ascii_list = []
    for i in range(0, len(message)):
        message_letter_list.append(ord(message[i]))
        element_ascii = message_letter_list[i]
        key_value = random.randint(10, 50)
        new_ascii = element_ascii + key_value
        while new_ascii in ascii_list:
            key_value = random.randint(10, 50)
            new_ascii = element_ascii + key_value
        decode_key.append(str(key_value))
        ascii_list.append(new_ascii)
        message_letter_list[i] = new_ascii
        # if 97 <= message_letter_list[i] <= 122:
        #     while new_ascii > 122:
        #         new_ascii = element_ascii + key - 123 + 97
        #     message_letter_list[i] = new_ascii
        #     # else:
        #     #     message_letter_list[i] = new_ascii
        # elif 65 <= message_letter_list[i] <= 90:
        #     while new_ascii > 90:
        #         new_ascii = element_ascii + key - 91 + 65
        #     message_letter_list[i] = new_ascii
        # else:
        #     pass
    new_message = ""
    for element in message_letter_list:
        new_message += chr(element)
    key = ""
    for values in decode_key:
        key += values
    print(new_message)
    print(key)


def decode(message, decodeKey):
    message_letter_list = []
    decode_key_list = []
    decodeKeylen = len(decodeKey)
    i = 0
    while i<decodeKeylen-1:
        key = int(decodeKey[i] + decodeKey[i+1])
        decode_key_list.append(key)
        i+=2
    for i in range(0, len(message)):
        message_letter_list.append(ord(message[i]))
        element_ascii = message_letter_list[i]
        key_value = decode_key_list[i]
        new_ascii = element_ascii - key_value
        message_letter_list[i] = new_ascii
    new_message = ""
    for element in message_letter_list:
        new_message += chr(element)
    print(new_message)




# def decode(message):
#     message_letter_list = []
#     for i in range(0, len(message)):
#         message_letter_list.append(ord(message[i]))
#         element_ascii = message_letter_list[i]
#         new_ascii = element_ascii - shift_value
#         if 97 <= message_letter_list[i] <= 122:
#             while new_ascii < 97:
#                 new_ascii = element_ascii - shift_value + 123 - 97
#             message_letter_list[i] = new_ascii
#             # else:
#             #     message_letter_list[i] = new_ascii
#         elif 65 <= message_letter_list[i] <= 90:
#             while new_ascii < 65:
#                 new_ascii = element_ascii - shift_value + 91 - 65
#             message_letter_list[i] = new_ascii
#         else:
#             pass
#     new_message = ""
#     for element in message_letter_list:
#         new_message += chr(element)
#     print(new_message)


print("Welcome to caeser cipher program.")
command = input("Type e for encode and d for decode: ").lower()
if command == "e":
    message = input("Enter the message to encode: ")
    # shift_value = int(input("Enter the shift value: "))
    encode(message)
elif command == "d":
    message = input("Enter the message to decode: ")
    decodeKey = input("Enter the decode key: ")
    decode(message, decodeKey)
os.system("pause")
