TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("what is your name? ")
    num_tickets = input("How many tickets would you like, {}?  ".format(name))
    # Expect a ValueError to happen and handle it appropriatly..
    try:
        num_tickets - int(num_tickets)
    except ValueError:
        print("Oh no, we ran into an issue. Please try again")
    num_tickets = int(num_tickets)
    amount_due = num_tickets * TICKET_PRICE
    print("The total due is ${}".format(amount_due))
    should_proceed = input("Do you want to proceed? Y/N ")
    if should_proceed.lower() == "y":
        # todo: Gather credit car information and process it.
        print("SOLD!")
        tickets_remaining -= num_tickets
    else:
        print("Thank you anyways. {}".format(name))
print("Sorry the tickets are all sold out!!!")