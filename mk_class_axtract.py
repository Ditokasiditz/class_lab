class Product:
    def __init__(self, Name, ImageURL, Price, Description, Calories):
        self._Name = Name
        self._ImageURL = ImageURL
        self._Price = Price
        self._Description = Description
        self._Calories = Calories


class Cart_Item:
    def __init__(self, Quantity, Discount,Name, ImageURL, Price ):
        self._Quantity = Quantity
        self.Discount = Discount
        self._Name = Name
        self._ImageURL = ImageURL
        self._Price = Price



