 
import csv

#item1= 'Phone'
#item1_price =100
#item1_quantity =5
#item1_price_total = item1_price*item1_quantity
#print(type(item1))#str
#print(type(item1_price))#int
#print(type(item1_quantity))#int
#print(type(item1_price_total))#int 
class Item:
  pay_rate =0.8 # The pay rate after 20% discount
  all=[]
  def __init__(self,name:str,price:float,quantity):
      #Run validations to the recived argument
      assert price>=0, f"Price {price} is not greater than zero!"
      assert quantity>=0 ,f"quantity {quantity} is not greater than zero!"

      # Assign to self object 
      self.name =name
      self.price =price
      self.quantity =quantity
      #print(f"An instance created: {name}")
      #def calculate_total_price(self,x,y):

      # Actions to execute
      Item.all.append(self)
  def calculate_total_price(self):
      return self.price * self.quantity
  def apply_discount(self):
     self.price = self.price * self.pay_rate


#item1 =Item("phone",100 ,-5) this is done to explain assert 
#item1 =Item("phone",100 ,5)
#item1.name ="Phone"
#item1.price =100
#item1.quantity =5
#print(item1.calculate_total_price(item1.price,item1.quantity))

#item2 =Item("Laptop",1000,3)
#item2.name ="Laptop"
#item2.price =1000
#item2.quantity =3
#print(item2.calculate_total_price(item2.price,item2.quantity))


#print(item1.name)
#print(item1.price)
#print("")
#print(item1.quantity)
#print(item2.name)
#print(item2.price)
#print(item2.quantity)
#print(item2.quantity)
#item2.has_numped =False
#print(item1.calculate_total_price())
#print(item2.calculate_total_price())
#print(Item.pay_rate)
#print(item1.pay_rate)
#print(item2.pay_rate)
#print(Item.__dict__) # All the attributes for Class level 
#print(item1.__dict__)# All the attributes for instance level
#item1.apply_discount()
#print(item1.price)

#item2=Item("laptop",1000,3)
#item2.pay_rate =0.7
#item2.apply_discount()
#print(item2.price)
  @classmethod
  def instantiate_from_csv(cls):
    with open('item.csv','r') as f:
     reader =csv.DictReader(f)
     items =list(reader)

     for item in items:
        Item (
           name =item.get('name'),
           price=float(item.get('price')),
           quantity=int(item.get('quantity')),
        )
    @staticmethod
    def is_integer(self):
           
     
     def __repr__(self):
       return f"Item('{self.name}',{self.price},{self.quantity})"
Item.instantiate_from_csv()
      
#item1 =Item("phone",100,1)
#item1 =Item("laptop",1000,3)
#item1 =Item("Cable",10,5)
#item1 =Item("Mouse",50,5)
#item1 =Item("Keyboard",75,5)
#print(Item.all)

#for instance in Item.all:
  # print(instance.name)


  #### Class Vs Static Methods ######

