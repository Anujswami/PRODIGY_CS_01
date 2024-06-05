#Encryption and Decryption using caesar cipher

def encrypt(text):
    encrypted_text = ""
    
    for letter in text:
        if letter == " ":
            encrypted_text += " "
        elif 'a' <= letter <= 'z':
            # Shift character and wrap around if necessary
            encrypted_text += chr((ord(letter) - ord('a') + 3) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            # Shift character and wrap around if necessary
            encrypted_text += chr((ord(letter) - ord('A') + 3) % 26 + ord('A'))
        else:
            # Non-alphabetic characters are added unchanged
            encrypted_text += letter
    
    return encrypted_text

def decrypt(encrypted_text):
    decrypted_text = ""
    
    for letter in encrypted_text:
        if letter == " ":
            decrypted_text += " "
        elif 'a' <= letter <= 'z':
            # Shift character and wrap around if necessary
            decrypted_text += chr((ord(letter) - ord('a') - 3) % 26 + ord('a'))
        elif 'A' <= letter <= 'Z':
            # Shift character and wrap around if necessary
            decrypted_text += chr((ord(letter) - ord('A') - 3) % 26 + ord('A'))
        else:
            # Non-alphabetic characters are added unchanged
            decrypted_text += letter
    
    return decrypted_text
choice=int(input("Press 1 for Encryption\nPress 2 for Decryption:\n"))
if(choice==1):
    Plain_text = input("Enter the text for Encryption: ")
    encrypted_text = encrypt(Plain_text)
    print("The cipher text is:\n\n:-", encrypted_text)
elif(choice==2):
    Cipher_text = input("Enter the text for Decryption: ")
    decrypted_text = decrypt(Cipher_text)
    print("The Plain text is\n\n:-", decrypted_text)
else:
    print("---------------You have entered the wrong choice----------------")
    






    