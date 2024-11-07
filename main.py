# This is a blind auction program

# Function to loop through a dictionary and determine the winner
def find_highest_bidder(bidding_dictionary):
    highest_price = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_price:
            highest_price = bid_amount
            winner = bidder
    # Printing the winner of the auction
    print(f"The winner is {winner} with a bid of ${highest_price}")


bids_dict = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid? "))
    bids_dict[name] = price
    # print(bids_dict)
    other_bidder = input("Is there any other bidder? Type 'yes' or 'no' \n").lower()
    if other_bidder == "no":
        continue_bidding = False
        find_highest_bidder(bids_dict)
    elif other_bidder == "yes":
        # Print statement to clear screen after every bidder submit their bids
        print("\n" * 300)
