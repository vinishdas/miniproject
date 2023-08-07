import random
import string
 
def genrator(le,num,sym):
     password=[]
     for i in range(le):
        password.append(random.choice(string.ascii_letters))
     for i in range(num):
          password.append(random.randint(0,9))
     for i in range(sym):
          password.append(random.choice(string.punctuation))
     random.shuffle(password)
     print("this is your password as per your requirment: ")
     passw = ' '.join(map(str, password))
     new_pass = "".join(passw.split())
     print(new_pass)
     

print("welcome to the password generator  ")
print("how many letters do you want in your password? : ",end =' ')
letter = int(input())
print("How many numbers do you want in your password? ",end =' ')
numbers = int(input())
print("how mnay symbols do you want in your password?",end=' ')
symbols= int(input())
genrator(letter,numbers,symbols)