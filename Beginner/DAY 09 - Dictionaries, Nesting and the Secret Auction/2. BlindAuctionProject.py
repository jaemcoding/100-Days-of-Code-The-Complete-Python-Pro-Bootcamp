from art import logo
print(logo)

data = {}
need_new_bids = True

while need_new_bids:
# TODO-1: Ask the user for input
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    data[name] = price
    # TODO-3: Whether if new bids need to be added
    new_bids = input("Are there any other bidders? Type 'Yes' or 'No'.\n").lower()
    if new_bids == 'no':
        need_new_bids = False
    print("\n" * 20)
    
# TODO-4: Compare bids in dictionary
highest_bid = 0
winner = ""

for bidder in data:
    bid_amount = data[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}!")