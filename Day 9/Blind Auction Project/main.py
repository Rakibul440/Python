
from art import logo
print(logo)

bidders = {}
bidders_details = {
    "name" : [],
    "price" : []
}

bid_again = True
while bid_again :
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    # bidders[name] = price
    bidders_details["name"].append(name)
    bidders_details["price"].append(price)
    # TODO-3: Whether if new bids need to be added
    any_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if any_bidders == 'yes':
        bid_again = True
        print('\n'*20)
    else:
        bid_again = False

# TODO-4: Compare bids in dictionary
print(bidders_details)

highest_bid = max(bidders_details["price"])
index = bidders_details["price"].index(highest_bid)
bidders_name = bidders_details["name"][index]

print(f"The winner is {bidders_name} with a bid of ${highest_bid}")

