class Person:
    #initializes
    def __init__(self,name, age, address, phonenumber):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phonenumber = phonenumber
#gets and sets name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
#gets and sets age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
#gets and sets address
    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address
#gets and sets phonenumber
    def get_phonenumber(self):
        return self.__phonenumber
    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

