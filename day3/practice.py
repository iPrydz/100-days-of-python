# IF / ELSE
height = 120

if height > 100:
    print("¡Qué alto!")
else:
    print("Qué bajito haha")

# Reverse
not height > 10

height = bill = 0

height = int(input("What's your height (cm)? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What's your age? "))
    if age < 12:
        bill = 5
        print ("Child tickets are $5.")
    elif age < 18:
        bill = 7
        print ("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print ("People with midlife crisis doesn't pay for tickets ;-)")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y": bill += 3

print(f"The total bill is ${bill}.")

#Hay una forma de que ignore los apóstrofes en los strings usando \ e ignorará la siguiente letra

print('You\'re... Type "left" or "right"')