alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

def encrypt(original_text,shift_amount):
    encrypted_text = ""
    for i in range(len(original_text)):
        letter = original_text[i]
        index = 0
        if letter == " ":
            encrypted_text += " "
        else :
            for j in range(len(alphabet)):
                if letter == alphabet[j]:
                    index = j+shift_amount
            # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
            if index > 25 :
                encrypted_text += alphabet[index - 26]
            else:
                encrypted_text += alphabet[index]
    print(f"Here is the encoded result: {encrypted_text}")

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt(text,shift)



