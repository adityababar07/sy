# finding no. of vowels

text = input("enter the text:\t")
text = text.lower()

vowels = ['a', 'u', 'e', 'i', 'o']

no_of_vowels =0
no_of_whitespaces =0
no_of_fullstopes =0
no_of_semicolan =0
no_of_comma =0
no_of_a = 0
no_of_e = 0
no_of_i = 0
no_of_o = 0
no_of_u = 0



for i in vowels:
    for letter in text:
        if letter == i:
            no_of_vowels+=1
            if letter == 'a':
                no_of_a += 1
            
        elif letter == " ":
            no_of_whitespaces+=1
        elif letter == ".":
            no_of_fullstopes+=1
        elif letter == ";":
            no_of_semicolan+=1
        elif letter == ",":
            no_of_comma+=1

print(f"\n\nThe no. of vowels is {no_of_vowels}, \nthe no. of whitespace is {no_of_whitespaces}, \nthe no. of semicolon is {no_of_semicolan}, \nthe no. of fullstop is {no_of_fullstopes}, and \nthe no. of comma is {no_of_comma}.")

'''
Output :-
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/vowel.py
enter the text: Encryption is an integral part of our daily lives – whether you are sending messages to friends on WhatsApp, visiting a website and your browser is making sure it's legitimate, or entering your bank details when buying something online. Encryption protects your data from potentially malicious and prying eyes.


The no. of vowels is 95, 
the no. of whitespace is 240, 
the no. of semicolon is 0, 
the no. of fullstop is 10, and 
the no. of comma is 10.
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''
        
