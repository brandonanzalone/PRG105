from employee import employee
class productionworker(employee):

    def __init__(self,name,number,shiftnumber,hourly):

        employee.__init__(self,name,number)
        self.__shiftnumber = shiftnumber
        self.__hourly = hourly
#setters
    def set_shiftnumber(self,shiftnumber):
        self.__shiftnumber = shiftnumber

    def set_hourly(self,hourly):
        self.__hourly = hourly
#getters
    def get_shiftnumber(self):
        return self.__shiftnumber

    def get_hourly(self):
        return self.__hourly
