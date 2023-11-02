alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def messages():
    global direction
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode" or direction == "decode":
        print(f"\nThe result is {caesar(text, shift)}")
        decide()
    else:
        print("Undefined")
        decide()

def caesar(text, shift) -> str:

    final = ""

    if direction == "decode":
        shift *= (-1)
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            position_final = (position + shift) % 26
            letter_final = alphabet[position_final]
            final += letter_final
        else:
            print("Unknown")
            final += letter

    return final


def decide():
    message = input("Do you want to continue? Type yes or no. ").lower()
    if message == "yes":
        messages()
    elif message == "no":
        print("End of the programm")
    else:
        print("Unknown")

messages()