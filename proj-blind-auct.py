import art

print(art.bidding_logo)

def find_highest_bid(bidding_dict):
    winner = ""
    highest_bid= 0
    for bidder in bidding_dict:
        bid_amount= bidding_dict[bidder]
        if bid_amount >highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the price of ${highest_bid}.")

bids = {}

while True:
    name = input("Enter Your name: ")
    price = int(input("Enter your price: $ "))
    bids[name] = price
    ch= input("Are there any other bidders? ")
    if ch=='no'.lower():
        find_highest_bid(bids)
    else:
        print("\n"*20)

