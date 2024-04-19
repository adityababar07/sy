decrypted = b"abcdefghijklmnopqrstuvwxyz{:!'@#$%^&*()_|+=-?/12,345678 90"
encrypted = b"poilkjuyhgtrfedswaqzxcmvbn}[{07982()14653+/*-?.<,>@#!$^% |"

encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)

result = ''
choice = ''
message = ''

while choice != '0':
    choice = input("\n Do you want to encrypt or decrypt the message?\n 1 to encrypt, 2 to decrypt or 0 to exit program. :\t ")

    if choice == '1':
        message = input('\nEnter message for encryption: ')
        result = message.translate(encrypt_table)
        print('\n output :- \n' + result + '\n\n')

    elif choice == '2':
        message = input('\nEnter message to decrypt: ')
        result = message.translate(decrypt_table)
        print(result + '\n\n')

    elif choice != '0':
        print('You have entered an invalid input, please try again. \n\n')