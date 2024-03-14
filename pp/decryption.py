def decrypt(text):
    
    data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '!', '@', '#', '$', '%', '^', '?', ':', '&', '.', ',', '/' ,'\\','\'','"', ';' ]
    
    cipher = []
    output_text =""

    with open("cipher.txt", 'r') as f:
        code = f.read()

    for i in code:
        cipher.append(i) 
    
    for i in text:
        index = cipher.index(i)
        output_text+= data[index]

    print(f"Decrypted text is :\t{output_text}")
