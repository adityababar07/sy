import random as rd


def encrypt(text):
    data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '!', '@', '#', '$', '%', '^', '?', ':', '&', '.', ',', '/' ,'\\','\'','"', ';' ]
    
    # cipher = rd.shuffle(data)
    cipher = rd.sample(data,62)
    
    
    print(cipher)
    
    # text = input("Enter your text:\t")
    
    output_text = ""
    
    
    for i in text:
        index = data.index(i)
        # print(cipher[index])
        output_text+= cipher[index]
    
        # element = output_text + cipher[index]
    
    print(f"The encrypted text is:-\n {output_text}")
    
    with open("cipher.txt", 'w+') as f:
        for i in cipher:
            f.write(i)
    
    with open("output.txt", 'w+') as f:
        f.write(output_text)
    



