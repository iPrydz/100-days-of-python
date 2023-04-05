print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100
number_people = int(input("How many people to split the bill? "))

percent_tip = 1 + percent_tip
bill *= percent_tip
bill /= number_people

total = "{:.2f}".format(bill) # Redondea a 2 dígitos y añade un 0 si hace falta.

print(f"Each person should pay: ${total}")