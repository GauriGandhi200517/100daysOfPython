# secret code decoder
def decode_secret_code(code):
    # Simple Caesar cipher decoder with shift of 3 (example)
    decoded = ""
    for char in code:
        if char.isalpha():
            shift = 3
            base = ord('a') if char.islower() else ord('A')
            decoded += chr((ord(char) - base - shift) % 26 + base)
        else:
            decoded += char
    return decoded

# Example usage
secret_word = "gauri"
encoded_word = ""
for char in secret_word:
    if char.isalpha():
        shift = 3
        base = ord('a') if char.islower() else ord('A')
        encoded_word += chr((ord(char) - base + shift) % 26 + base)
    else:
        encoded_word += char

print("Encoded word:", encoded_word)
print("Decoded word:", decode_secret_code(encoded_word))