class employee(object):
    """description of class"""
    def __init__(self,name,number):
        self.__name = name
        self.__number = number
#setters
    def set_name(self,name):
        self.__name = name

    def set_number(self,number):
        self.__number = number
#getters
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


