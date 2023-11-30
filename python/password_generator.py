import random
import string
 
def genrator(le,num,sym):
     passw= ''
     print("this is your password as per your requirment: ")
     for i in range(le):
        passw+=random.choice(string.ascii_letters)
     for i in range(num):
          passw+=str(random.randint(0,9))
     for i in range(sym):
         passw+=random.choice(string.punctuation)
     print(''.join(random.sample(passw,len(passw))))
      
     
print("""    ___                                    _                                   _             
   / _ \__ _ ___ _____      _____  _ __ __| |   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
  / /_)/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 / ___/ (_| \__ \__ \\ V  V / (_) | | | (_| | | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \/    \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                               |___/                                         ,""")
print("welcome to the password generator  ")
print("how many letters do you want in your password? : ",end =' ')
letter = int(input())
print("How many numbers do you want in your password? ",end =' ')
numbers = int(input())
print("how mnay symbols do you want in your password?",end=' ')
symbols= int(input())
genrator(letter,numbers,symbols)
