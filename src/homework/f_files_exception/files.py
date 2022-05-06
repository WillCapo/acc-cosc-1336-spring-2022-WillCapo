inventory = {'Soup': 10}

def add_inventory(name, quantity):
    if name not in inventory:
        inventory[name] = quantity
        invFile = open('inventory.txt', 'w')
        invFile.write(str(inventory) + '\n')
        invFile.close()
        print('Done 1')
    else:
        inventory[name] += quantity
        invFile = open('inventory.txt', 'w')
        invFile.write(str(inventory) + '\n')
        invFile.close()
        print('Done 2')
    return inventory

def display_inventory(file):
    file = open('inventory.txt', 'r')