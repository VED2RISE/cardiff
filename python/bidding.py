
def captions():
    print("Welcome to the secret auction program")
    bidds = {}

    while True:
        name = str(input("What is your name? "))
        bid = float(input("What's your bid? " ))
        decision = str(input("Are there any other bidders? Type yes or no. "))
        bidds[name] = bid

        if decision.lower() != "yes":
            break

    max_value = max(bidds.values())
    keys_for_value = [key for key, value in bidds.items() if value == max_value]

    if len(keys_for_value) == 1:
        print(f"The winner is {keys_for_value[0]} with a bid of {max_value}")
    else:
        print(f"We have several winners: {", ".join(keys_for_value)} each with a bid of {max_value}")


captions()

