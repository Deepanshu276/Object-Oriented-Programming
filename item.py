import csv
class Item:
    discount=0.2 #class attribute
    all=[]
    def __init__(self,name:str, __price:float, quantity=0 ):
        #assert method is used for validation
        assert __price>0 ,f"__price {__price} should be greater than zero "
        assert quantity>0, f"Quantity should be greater than zero"

        self.__name=name
        self.__price=__price
        self.quantity=quantity

        #storing all the instance of the class
        Item.all.append(self)
    @property
    def price(self):
        return self.__price

    def discount___price(self):
        self.__price=self.__price *self.discount
        return self.__price
    def apply_increment(self,increment_value):
        self.__price=self.__price +self.__price*increment_value
        return self.__price
    @property 
    #Property Decorator= Read Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name=value   
    def total___price(self):
        return self.__price*self.quantity
        
    
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv', 'r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                __price=float(item.get('__price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        #we will count out the fliat that are point zero
        #eg 5.0,10.0
        if isinstance(num,float):
            #Count out the float that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


    #For Representing the instance 
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
    def __connect(self,smtp_server):
        pass
    def __prepare_body(self):
        return """
        Hello Someone.
        We have {self.name} {self.quantity} times
        regards, 
        """
    def __send(self):
        pass

    def send_mails(self):
        self.__connect(" ")
        self.__prepare_body()
        self.__send()





#print(Item.all)

#Item.load_data_from_csv()
#print(Item.all)
#print(Item.is_integer(7))


"""item1=Item("Phone", 100, 1)
item2=Item("Laptop", 1000,3)
item3=Item("Cable", 10, 5)
item4=Item("Mouse",50,6)
item5=Item("Keyboard", 75, 5)"""

#For viewing all the items stored in our list
#for instance in Item.all:
 #   print(instance.name)



#item=Item("Computer",23,21)
#item1=Item("Laptop", 90, 12)
#print(item.discount___price())
#item1.discount=0.1 # if you want to apply different discount for different product(overwriting)
#print(item1.discount___price())




#print(Item.__dict__) viewing all the variable present in class Item(class variable + instance variable)
#print(item.__dict__) viewing all the variable present in instance item(instance variable)
#total_amount=item.total___price() calcualting total amount and storing it in tha variable
#print(total_amount)
#print(item.discount___price(total_amount)) calculating the discount on total amount

#print(item.name,item.__price,item.quantity)
#print(item1.name,item1.__price,item1.quantity)
#print(item1.total___price())
