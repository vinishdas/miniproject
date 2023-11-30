import time
# from pydub import AudioSegment
# from pydub.playback import play
# beep = AudioSegment.from_file("vinishdas/miniproject/audio/beep-07a.mp3",format="mp3")
# boop = AudioSegment.from_file("vinishdas/miniproject/audio/beep-08b.mp3",format="mp3")

 
morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..'
}

def TextToMor():
    print("\nenter the text you want to convert: ",end='')
    text = input()
    for i in text:
        for j in morse_code_dict.get(i,"null"):
             if(j == '.'):
                print(j,end='')
                time.sleep(0.5)
                # play(beep)
             else:
                print(j,end='')
                time.sleep(0.5)
                # play(boop)
        print(' ',end='')
    print('\n')
def MorToText():
    print("\nenter the morse code with space for letter: ",end='')
    text = input().split()
    for i in text:
        for key ,value in morse_code_dict.items():
             if(value == i):
                print(key,end='')
            #  else:print("null",end='')
    print('\n')

print("MENU\n")
print(" Type 1 to convert text to morse Code")
print(" Type 2 to convert morse Code to text")
print(" Type 3 to exit\n\n")
while(True):
    print("enter your choice: ",end = '')
    choice= int(input())
    if(choice ==1):
        TextToMor()
    elif(choice ==2):
        MorToText()
    elif(choice ==3):
            exit()
            
    else:print("invalid \n")
    





