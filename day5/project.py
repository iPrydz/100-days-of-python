# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

table = [letters, numbers, symbols]
table_nr = [nr_letters, nr_numbers, nr_symbols]
random_nr = 0
password = ""


while table_nr[0] > 0 or table_nr[1] > 0 or table_nr[2] > 0:
    random_nr = random.randint(0, 2)
    
    if table_nr[random_nr] > 0:
        if random_nr == 0:
            password = password + str(table[random_nr][random.randint(0, len(letters) - 1)])
        if random_nr == 1:
            password = password + str(table[random_nr][random.randint(0, len(numbers) - 1)])
        if random_nr == 2:
            password = password + str(table[random_nr][random.randint(0, len(symbols) - 1)])
        table_nr[random_nr] -= 1

print (password)