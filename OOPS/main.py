from Item import Item

#se
item1 = Item("MYItem",750)
item1.name="OtherItem"
#item1.apply_increment(0.2)
item1.apply_discount()

print(item1.name)