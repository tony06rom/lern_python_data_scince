Inventory = {'gold': 999, 'gun': 3, 'water': 5, 'meat': 7, 'health': 2, 'stuff': 10}

dragonLoot = ['gold', 'gun', 'water', 'gold', 'stuff', 'gun', 'health', 'gold']

def addToInventory(inventory, addedItems):


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(k + ' = ' + str(v))
        item_total += v
    print('Total number of items: ' + str(item_total))

displayInventory(Inventory)


"""def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(k + ' = ' + str(v))
        item_total += v
    print('Total number of items: ' + str(item_total))

displayInventory(Inventory)"""

