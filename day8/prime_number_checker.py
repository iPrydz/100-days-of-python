#Write your code below this line 👇

def prime_checker(number):
    not_prime = True
    for num in range(2, number):
        if number % num == 0:
            not_prime = False
    if not_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
            

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)