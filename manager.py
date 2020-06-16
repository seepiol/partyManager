from dboperations import *

while True:
    r = display_items_id()
    for i in r:
        if i[2] == 1:
            pass
        else:
            print(f"{i[0]}) {i[1]} ")
    id = input("Which item is Out of Stock? :")
    makeOutOfStock(id)