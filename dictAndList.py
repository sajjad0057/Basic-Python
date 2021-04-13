def addToInentory(inventory,addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item]=inventory[item]+1
    return inventory

def displayInventory(inv):
    print("Inventory:")
    total_item = 0
    for key,value in inv.items():
        print(f'{value} {key}')
        total_item +=value
    print("Total number of Items :",total_item)
inv = {'gold_coin':42,'rope':1}
dragon_lot = ['gold_coin','dagger','gold_coin','gold_coin','ruby']
x=addToInentory(inv,dragon_lot)
displayInventory(x)