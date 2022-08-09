from item import Item

item1=Item("MyItem", 750,1)
item1.apply_increment(0.2)
print(item1.price)
item1.send_mails()


