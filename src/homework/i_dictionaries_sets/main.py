import dictionary

def menu():
    choice = input('\nMenu\n\n1-Add or update item\n2-Remove item\n3-Exit\n\nPlease choose an option: ')
    if choice == '1':
        add_item()
    elif choice == '2':
        del_item()
    else:
        print('\nExiting . . .\n')

def add_item():
    print('\nCURRENT INVENTORY\n' + str(dictionary.inventory))
    key = input('\nPlease enter an item name: ')
    quantity = int(input('\nPlease enter inventory changes: '))
    print('\nNEW INVENTORY\n' + str(dictionary.add_inventory(key, quantity)))
    choice = input('\nWould you like to continue?\n\n1-Menu\n2-Exit\n\nPlease choose an option: ')
    if choice == '1':
        menu()
    else:
        print('\nExiting . . .\n')

def del_item():
    print('\nCURRENT INVENTORY\n' + str(dictionary.inventory))
    key = input('\nPlease enter an item name: ')
    print('\nNEW INVENTORY\n' + str(dictionary.remove_inventory(key)))
    choice = input('\nWould you like to continue?\n\n1-Menu\n2-Exit\n\nPlease choose an option: ')
    if choice == '1':
        menu()
    else:
        print('\nExiting . . .\n')

menu()