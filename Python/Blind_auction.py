print("Welcome to the secret auction program.")
bids = {}
should_continue = True

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the bid of ${highest_bid}")

while should_continue:
  name = input("What is your name?: ")
  price = int(input("What's your bid?: $"))
  bids[name] = price
  ask_for_user = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if ask_for_user == "yes":
    clear()
  elif ask_for_user == "no": 
    should_continue = False
    highest_bidder(bids)
