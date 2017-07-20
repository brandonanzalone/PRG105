class OfficeFurniture(object):
    """description of class"""
#initialization
    def __init__(self,category,material,length,width,height,price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price
#setters
    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price


#getters
    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price
#Format object into string and return it
    def __str__(self):
        line_item = "The "+ self.__category + " is made of " + self.__material +"." + "\n"+"With a length of " + format(self.__length,'.1f') + " inches.\n" + "A Height of " + format(self.__width,'.1f') + " inches.\n" + "And a Width of " + format(self.__height,'.1f') + " inches.\n" + "At a price of $" + format(self.__price, '.2f') + "."
        return line_item



 


