class Product:
    def __init__(self, Name, ImageURL, Price, Description, Calories, Option):
        self._Name = Name
        self._ImageURL = ImageURL
        self._Price = Price
        self._Description = Description
        self._Calories = Calories
        self._Option = []                   #from Option_Product class


class Option_Product:
    def __init__(self, Name, ImageURL):
        self._Name = Name
        self._ImageURL = ImageURL


class Cart_Item:
    def __init__(self, Quantity, Discount,Name, ImageURL, Price ):
        self._Quantity = Quantity
        self._Discount = Discount
        self._Name = Name                   #from class product
        self._ImageURL = ImageURL
        self._Price = Price


class Cart:
    def __init__(self, Shipping_Cost , Total_Cost, Cart_Item,Quantity, Discount, Price):
        self._Shipping_Cost = Shipping_Cost
        self._Total_Cost = Total_Cost
        self._Cart_Item = []               #list of item in cart 
        self._Quantity = Quantity
        self._Discount = Discount
        self._Price = Price


class Admin:
    def __init__(self, Id, Name ,Email, Product):
        self._Id = Id
        self._Name = Name
        self._Email = Email        


class Categiry_Menu:
    def __init__(self, Name_category, Image_Category,Product):
        self._Name_category = Name_category
        self._Image_Category = Image_Category
        self._Product = []


class Account:
    def __init__(self, Id, Email, Shipping_Address, Phone):
        self._Id = Id
        self._Email = Email
        self._Shipping_Address = Shipping_Address
        self._Phone = Phone 


class User:
    def __init__(self, Id, Password, Status, Account):
        self._Id = Id
        self._Password = Password
        self._Status = Status
        self._Account = Account             #list of Account


class Order:
    def __init__(self, Shipping_Address, Total_Cost, Status, Payment_Status):
        self._Shipping_Address = Shipping_Address
        self._Total_Cost = Total_Cost
        self._Status = Status
        self._Payment_Status = Payment_Status           #from clss payment


class Payment:
    def __init__(self, Status, Date_time, Transaction_id):
        self._Status = Status
        self._Date_time = Date_time
        self._Transaction_id = Transaction_id


class Cash(Payment):
    def __init__(self, Status, Date_time, Transaction_id,Cash_Tendered):
        Payment.__init__(Status, Date_time, Transaction_id)
        self._Cash_Tendered = Cash_Tendered


class Credit_Debit_card(Payment):
    def __init__(self, Status, Date_time, Transaction_id, Card_number, Name, Cvv):
        Payment.__init__(Status, Date_time, Transaction_id)
        self._Card_number = Card_number
        self._Name = Name
        self._Cvv = Cvv


class PaymentStatus(enumerate):
    UNPAID, COMPLETED, DECLINED, CANCELLED = 1, 2, 3, 4


class UserStatus(enumerate):
    ACTIVE, BLOCKED, BANNED, UNKNOWN = 1, 2, 3, 4
         

class OrderStatus(enumerate):
    PENDING, COMFIRM, CANCELLED, DELIVERED = 1, 2, 3, 4
