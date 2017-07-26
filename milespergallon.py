import tkinter
import tkinter.messagebox

class CalculateMilesPerGallon :
    def __init__(self):
        self.parent_widget = tkinter.Tk()

        self.MPG = tkinter.StringVar()


        self.gallons_frame = tkinter.Frame(self.parent_widget)
        self.miles_frame = tkinter.Frame(self.parent_widget)
        self.calculate_frame = tkinter.Frame(self.parent_widget)


        self.entry_gallons = tkinter.Entry(self.gallons_frame)
        self.gallons_label = tkinter.Label(self.gallons_frame, text = 'Enter Gallons')

        self.entry_miles = tkinter.Entry(self.miles_frame)
        self.miles_label = tkinter.Label(self.miles_frame, text = 'Enter Miles')

        self.calculatebutton = tkinter.Button(self.calculate_frame, text = 'Calculate MPG', command = self.calculateMPG)
        self.MPG_label = tkinter.Label(self.calculate_frame, textvariable = self.MPG)    

        self.gallons_label.pack(side ='left')
        self.entry_gallons.pack(side ='right')

        self.miles_label.pack(side ='left')
        self.entry_miles.pack(side ='right')

        self.calculatebutton.pack(side = 'left')
        self.MPG_label.pack(side = 'right')

        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.calculate_frame.pack()

        tkinter.mainloop()

    def calculateMPG(self):
        milespergallon = int(self.entry_miles.get()) / int(self.entry_gallons.get())
        label = 'Miles Per Gallon :' + format(milespergallon,'.2f')
        self.MPG.set(label)

my_gui = CalculateMilesPerGallon()
