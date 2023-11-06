import time

morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..'
}

def TextToMor():
    print("enter the text you want to convert: ",end='')
    text = input()
    for i in text:
        print(morse_code_dict[i],end='')

print("MENU\n")
print(" Type 1 to convert text to morse Code")
print(" Type 2 to convert morse Code to text")
print(" Type 3 to exit\n\n")
while(True):
    print("enter your choice: ",end = '')
    choice= input()
    if(choice == 1):
        TextToMor()
    else:break
       





