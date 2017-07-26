import tkinter
import tkinter.messagebox
#class for window, for displaing translations
class MyFirstWindow :
    def __init__(self,):
        self.main_window = tkinter.Tk()
        self.one_value = tkinter.StringVar()
        self.two_value = tkinter.StringVar()
        self.three_value = tkinter.StringVar()
        self.four_value = tkinter.StringVar()
        self.five_value = tkinter.StringVar()
        #button frame
        self.button_frame = tkinter.Frame(self.main_window)

   

      
        #buttons
        self.one = tkinter.Button(self.main_window, textvariable =self.one_value, command = self.showone)
        self.one_value.set( 'Jeden')

        self.two = tkinter.Button(self.main_window, textvariable =self.two_value, command = self.showtwo)
        self.two_value.set( 'Dwa')

        self.three = tkinter.Button(self.main_window, textvariable =self.three_value, command = self.showthree)
        self.three_value.set( 'Trzy')

        self.four = tkinter.Button(self.main_window, textvariable =self.four_value, command = self.showfour)
        self.four_value.set( 'Czerty')

        self.five = tkinter.Button(self.main_window, textvariable =self.five_value, command = self.showfive)
        self.five_value.set( 'Pięć')

        
        #packing
        self.one.pack()
        self.two.pack()
        self.three.pack()
        self.four.pack()
        self.five.pack()
   

     
        self.button_frame.pack()


        tkinter.mainloop()
#routines for translations
    def showone(self):
        self.one_value.set('One')
    def showtwo(self):
        self.two_value.set('Two')
    def showthree(self):
        self.three_value.set('Three')
    def showfour(self):
        self.four_value.set('Four')
    def showfive(self):
        self.five_value.set('Five')

     




my_gui = MyFirstWindow()
       
