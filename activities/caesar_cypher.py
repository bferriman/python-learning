# Receive a message then encrypt it by shifting the characters by a requested amount to the right
# For example, A becomes D, B becomes E, etc.
# Decrypt the message back again

while True:
    user_message = input("Enter message to encrypt: ")
    if user_message.replace(" ", "").isalpha():
        break
    else:
        print("Message must contain letters only")

while True:
    try:
        shift_value = int(input("Enter shift value: "))
        break

    except ValueError:
        print("Shift value must be a number")

encrypted_message = ""

for char in user_message:
    if char.isspace():
        encrypted_message += char
    else:
        char_code = ord(char) + shift_value
        if char.isupper():
            if char_code > 90:
                char_code -= 26
            elif char_code < 65:
                char_code += 26
        else:
            if char_code > 122:
                char_code -= 26
            elif char_code < 97:
                char_code += 26
        encrypted_message += chr(char_code)

print("Your encrypted message: ", encrypted_message)

decrypted_message = ""

for char in encrypted_message:
    if char.isspace():
        decrypted_message += char
    else:
        char_code = ord(char) - shift_value
        if char.isupper():
            if char_code > 90:
                char_code -= 26
            elif char_code < 65:
                char_code += 26
        else:
            if char_code > 122:
                char_code -= 26
            elif char_code < 97:
                char_code += 26
        decrypted_message += chr(char_code)

print("Your decrypted message: ", decrypted_message)
