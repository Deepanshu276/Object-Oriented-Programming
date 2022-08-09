from item import Item
class Phone(Item):
    
    def __init__(self,name:str, price:float, quantity=0,broken_phones=0):
        #Call to super function to have access to all attributes/ methods of parent class
        super().__init__(name,price,quantity)
        #Run validation to the received arguemnet
        assert broken_phones>=0, f"Broken Phones {broken_phones} is not greater than otr equal to zero"
        #assign to self object
        self.broken_phones=broken_phones


phone1=Phone("jscPhonev10",500,5,1)
print(Item.all)
print(Phone.all)