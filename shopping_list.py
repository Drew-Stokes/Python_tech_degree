# Create a new empty list named shopping_list
shopping_list = []
# Create a a function named add_to_list that declares a parameter named item
def add_to_list(item):
    # Add the item to the list
    shopping_list.append.item
def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
""")
    
show_help()
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue

    # Call add_to_list with new_item as an argument
    add_to_list(new_item)