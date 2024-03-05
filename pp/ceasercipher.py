from encryption import encrypt


while True:

    print('''What do you want to do ?

                1)Encrypt 
                2)Decrypt

            press what you want to do!!!!!
        ''')

    choice = int(input("enter what is your choice:\t")) 

    if choice == 1:

        text = input("Enter your text:\t")
        encrypt(text)


    elif choice == 2:

        text = input("enter your text :\t")
        decrypt(text)
