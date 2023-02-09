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


