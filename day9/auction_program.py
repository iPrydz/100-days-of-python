import os
import auction_program_art

bids = []
name = ""
bid = ""
other = "yes"

print(auction_program_art.logo)
print("Welcome to the secret auction program.\n")

def bid_program(name_input, bid_amount):
    name_input = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))

    new_person = {}
    new_person["name"] = name_input
    new_person["bid"] = bid_amount
    bids.append(new_person)

def calculate_bids():
    bigger = 0
    winner = ""
    for i in range(0, len(bids)):
        if bigger < bids[i]["bid"]:
            bigger = bids[i]["bid"]
            winner = bids[i]["name"]
    print(f"The winner is {winner} with a bid of ${bigger}")
    


while other == "yes":
    bid_program(name_input=name, bid_amount=bid)
    other = input("Are there any other bidders? Type 'yes' or 'no'. ")
    os.system('cls' if os.name == 'nt' else 'clear')
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    calculate_bids()
