Inventory = {'gold': 999, 'gun': 3, 'water': 5, 'meat': 7, 'health': 2, 'stuff': 10}

"""def displayInventory(item, number):
    print('Inventory:')
    numInventory = 0
    for k, v in item.items():
        numInventory = numInventory + v.get(number, 0)
    return numInventory

print(displayInventory(Inventory))
print('Total number of items: ' + str(displayInventory))"""

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(k + ' = ' + str(v))
        item_total += v
    print('Total number of items: ' + str(item_total))

displayInventory(Inventory)

