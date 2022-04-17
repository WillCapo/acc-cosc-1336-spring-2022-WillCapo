inventory = {'Soup': 10}

def add_inventory(key, quantity):
    if key in inventory:
        inventory[key] += quantity
    else:
        inventory[key] = quantity
    return inventory

def remove_inventory(key):
    if key in inventory:
        del inventory[key]
    return inventory