import tkinter
import tkinter.messagebox

class propertytax :
    def __init__(self):
        self.parent_widget = tkinter.Tk()

        self.landvalues = tkinter.StringVar()


        self.landvalue_frame = tkinter.Frame(self.parent_widget)
        self.calculate_frame = tkinter.Frame(self.parent_widget)


        self.entry_totallandvalue = tkinter.Entry(self.landvalue_frame)
        self.landvalue_label = tkinter.Label(self.landvalue_frame, text = 'Enter total property value. ')


        self.calculatebutton = tkinter.Button(self.calculate_frame, text = 'Property Tax', command = self.calculatepropertytax)
        self.propertytax_label = tkinter.Label(self.calculate_frame, textvariable = self.landvalues)    

        self.landvalue_label.pack(side ='left')
        self.entry_totallandvalue.pack(side ='right')

  
    

        self.calculatebutton.pack(side = 'left')
        self.propertytax_label.pack(side = 'right')

        self.landvalue_frame.pack()
        self.calculate_frame.pack()

        tkinter.mainloop()

    def calculatepropertytax(self):
        propertytaxowed = ((int(self.entry_totallandvalue.get()) *.60) / 100) *.75
        label = 'Property Tax : $' + format(propertytaxowed,'.2f')
        self.landvalues.set(label)

my_gui = propertytax()

