#This programs output will create a passwor for you, as per your needs
#you just have to enter the number of letters, numbers and symbols you need in the password
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to the PyPassword Generator !")
nr_letters = int(input("How many letters would you like in your password ? \n"))
nr_symbols = int(input("How many symbols would you like ?"))
nr_numbers = int(input("How many numbers would you like ? \n"))
password = []
for char in range(1,nr_letters+1):
                 password.append(random.choice(letters))

for char in range(1,nr_symbols+1):
                 password += random.choice(numbers)
                 
for char in range(1,nr_symbols+1):
                 password += random.choice(symbols)
                 
random.shuffle(password)

password_original = ""
for char in password:
                 password_original += char
                 
print(f"Your password is: {password_original}")
