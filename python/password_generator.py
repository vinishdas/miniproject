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
      
     

print("welcome to the password generator  ")
print("how many letters do you want in your password? : ",end =' ')
letter = int(input())
print("How many numbers do you want in your password? ",end =' ')
numbers = int(input())
print("how mnay symbols do you want in your password?",end=' ')
symbols= int(input())
genrator(letter,numbers,symbols)
