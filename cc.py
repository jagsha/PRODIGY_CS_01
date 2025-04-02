def caesar_cipher(Text, shift_value, mode="encrypt"):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''

    # Reverse shift for decryption
    if mode == "decrypt":
        shift_value = -shift_value  

    for char in Text:
        if char.lower() in alphabet:  
            x = char.lower()
            new_index = (alphabet.index(x) + shift_value) % 26  
            new_char = alphabet[new_index]

            # Preserve uppercase/lowercase
            output += new_char.upper() if char.isupper() else new_char
        else:
            output += char  # Keep non-alphabet characters unchanged

    return output

# Taking user input
Integer = int(input("Press 1 to encode the Text and Press 2 to decode: "))
Text = input("Enter the word: ")
shift_value = int(input("Enter the shift number: "))

# Encryption or Decryption based on user choice
if Integer == 1:
    result = caesar_cipher(Text, shift_value, "encrypt")
    print("Encrypted Text:", result)

elif Integer == 2:
    result = caesar_cipher(Text, shift_value, "decrypt")
    print("Decrypted Text:", result)

else:
    print("Invalid choice! Please enter 1 for encryption or 2 for decryption.")
