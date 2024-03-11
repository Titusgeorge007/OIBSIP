import string
import random
password_length=int(input("How long should the password length be?"))
print("Choose your prefered characters\n1.Alphabets\n2.Digits\n3.Special characters\n4.exit")
character_set=""
while True:
    choose=int(input("Enter a number"))
    if choose==1:
       character_set+=string.ascii_letter
    elif choose==2:
        character_set+=string.digits
    elif choose==3:
        character_set+=string.punctuation
    elif choose==4:
        break
    else:
        print("Enter a valid choice")
strong_password=''.join(random.choice(character_set)for i in range
(password_length))
print("The strong password is :", strong_password)