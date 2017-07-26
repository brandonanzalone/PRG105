import tkinter
import tkinter.messagebox

class MyFirstWindow :
    def __init__(self,):
        self.main_window = tkinter.Tk()
        self.name = tkinter.StringVar()
        self.street = tkinter.StringVar()
        self.state = tkinter.StringVar()

        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.name_label = tkinter.Label(self.info_frame, textvariable = self.name)
        self.street_label = tkinter.Label(self.info_frame, textvariable = self.street)
        self.state_label = tkinter.Label(self.info_frame, textvariable = self.state)

        self.name_label.pack()
        self.street_label.pack()
        self.state_label.pack()

        self.showinfobutton = tkinter.Button(self.main_window, text = 'Show info', command = self.showinfo)
        self.quitbutton = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)


        

        
       
        self.showinfobutton.pack(side ='left')
        self.quitbutton.pack(side ='right')

        self.info_frame.pack()
        self.button_frame.pack()


        tkinter.mainloop()

    def showinfo(self):
        self.name.set('Brandon Anzalone')
        self.street.set('3985 sandubury court')
        self.state.set('Crystal lake, IL 60156')




my_gui = MyFirstWindow()
       
