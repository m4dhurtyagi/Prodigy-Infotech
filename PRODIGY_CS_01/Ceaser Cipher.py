def encrypt(Text, n):
    encrypt_text = ""
    for i in range(len(Text)):
        c = Text[i]
        if c == " ":
            encrypt_text += " "
        elif (c.isupper()):
            encrypt_text += chr((ord(c)+ n-65)%26 + 65)
        elif (c.islower()):
            encrypt_text += chr((ord(c)+ n-97)%26 + 97)
        else:
            encrypt_text += c
    return encrypt_text

def decrypt(Text, n):
    decrypt_text = ""
    for i in range(len(Text)):
        c = Text[i]
        if c == " ":
            decrypt_text += " "
        elif (c.isupper()):
            decrypt_text += chr((ord(c)- n-65)%26 + 65)
        elif (c.islower()):
            decrypt_text += chr((ord(c)- n-97)%26 + 97)
        else:
            decrypt_text += c
    return decrypt_text

def main():
    Text = input("Enter Text : ")
    n = int(input("Enter Shift Value : "))
    print("SELECT")
    print("1 : Encrypt")
    print("2 : Decrypt")
    Choice = int(input("Enter Choice : "))
    
    if Choice == 1:
        print("Encrypted Text : " + encrypt(Text, n))
    elif Choice == 2:
        print("Decrypted Text : " + decrypt(Text, n))
    else:
        print("Enter Correct Choice")

print(30*"=" + " CAESAR CIPHER " + 30*"=")
while True:
    main()
    