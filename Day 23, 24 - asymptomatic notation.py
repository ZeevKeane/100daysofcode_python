
#cesar cipher - Brilliant: Programming with Python
alphabet = "abcdefghijklmnopqrstuvwxyz"

def cesar(letter, cesar_shift):
    letter_index = alphabet.index(letter)
    shifted_letter_index = cesar_shift + letter_index
    shifted_letter = alphabet[shifted_letter_index]
    return shifted_letter

print(cesar("g", 13))
