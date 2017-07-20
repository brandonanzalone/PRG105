from officefurniture import OfficeFurniture
#sub class
class Desk(OfficeFurniture):

    def __init__(self,category,material,length,width,height,price,location,number):

        OfficeFurniture.__init__(self,category,material,length,width,height,price)

        self.__location = location
        self.__number = number
#setters
    def set_location(self,location):
        self.__location = location

    def set_number(self,number):
        self.__number = number
#getters
    def get_location(self):
        return self.__location
    
    def get_number(self):
        return self.__number
#format object to string
    def __str__(self):
        line_item =OfficeFurniture.__str__(self) + "\n" + "The desk has drawers located on the "+ self.get_location() + " side.\n" + "The desk comes with " + str(self.get_number()) + " drawers."
        return line_item



