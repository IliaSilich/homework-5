def encrypt_caesar(message_to_encrypt, shift):
    encrypted_message = ""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for char in message_to_encrypt:
        if char.upper() in alphabet:
            shifted_index = (alphabet.index(char.upper()) + shift) % 26
            if char.islower():
                encrypted_message += alphabet[shifted_index].lower()
            else:
                encrypted_message += alphabet[shifted_index]
        else:
            encrypted_message += char

    return encrypted_message


def decrypt_caesar(message_to_decrypt, shift):
    decrypted_message = ""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for char in message_to_decrypt:
        if char.upper() in alphabet:
            shifted_index = (alphabet.index(char.upper()) - shift) % 26
            if char.islower():
                decrypted_message += alphabet[shifted_index].lower()
            else:
                decrypted_message += alphabet[shifted_index]
        else:
            decrypted_message += char

    return decrypted_message


message = input("Введите сообщение для шифрования: ")
shift_encrypt = int(input("Введите шаг шифрования (число от 1 до 25): "))
encrypted_text = encrypt_caesar(message, shift_encrypt)
print(f"Зашифрованное сообщение: {encrypted_text}")

encrypt_message = input("Введите зашифрованное сообщение: ")
shift_decrypt = int(input("Введите шаг дешифрования (число от 1 до 25): "))
decrypted_text = decrypt_caesar(encrypt_message, shift_decrypt)
print(f"Расшифрованное сообщение: {decrypted_text}")
