import tkinter
import tkinter.messagebox

class CustomerInterface(object):
    def __init__(self):
        global totalservicecost
        totalservicecost = 0 

        self.parent_widget = tkinter.Tk()

        self.totalservices = tkinter.StringVar()

        
        self.items1_frame = tkinter.Frame(self.parent_widget)
        self.items2_frame = tkinter.Frame(self.parent_widget)
        self.items3_frame = tkinter.Frame(self.parent_widget)
        self.items4_frame = tkinter.Frame(self.parent_widget)
        self.items5_frame = tkinter.Frame(self.parent_widget)
        self.items6_frame = tkinter.Frame(self.parent_widget)
        self.items7_frame = tkinter.Frame(self.parent_widget)

        self.totaling_frame = tkinter.Frame(self.parent_widget)


        self.item1_label = tkinter.Label(self.items1_frame, text = 'Printing services, $10.99. ')
        self.print1_button = tkinter.Button(self.items1_frame, text='Add ', command = lambda: self.addservice(10.99))

        self.item2_label = tkinter.Label(self.items2_frame, text = 'Consulting services, $2,000.00. ')
        self.print2_button = tkinter.Button(self.items2_frame, text='Add ', command = lambda: self.addservice(2000.00))

        self.item3_label = tkinter.Label(self.items3_frame, text = 'Shipping services, $5.40. ')
        self.print3_button = tkinter.Button(self.items3_frame, text='Add ', command = lambda: self.addservice(5.40))

        self.item4_label = tkinter.Label(self.items4_frame, text = 'Packaging services, $3.25. ')
        self.print4_button = tkinter.Button(self.items4_frame, text='Add ', command = lambda: self.addservice(3.25))

        self.item5_label = tkinter.Label(self.items5_frame, text = 'Recruting services, $1,000.00. ')
        self.print5_button = tkinter.Button(self.items5_frame, text='Add ', command = lambda: self.addservice(1000.00))

        self.item6_label = tkinter.Label(self.items6_frame, text = 'Marketing services, $1,500.00. ')
        self.print6_button = tkinter.Button(self.items6_frame, text='Add ', command = lambda: self.addservice(1500.00))

        self.item7_label = tkinter.Label(self.items7_frame, text = 'Training services, $200.00. ')
        self.print7_button = tkinter.Button(self.items7_frame, text='Add ', command = lambda: self.addservice(200.00))

      

        self.totalcost_label = tkinter.Label(self.totaling_frame, textvariable = self.totalservices)

        self.items1_frame.pack()
        self.items2_frame.pack()
        self.items3_frame.pack()
        self.items4_frame.pack()
        self.items5_frame.pack()
        self.items6_frame.pack()
        self.items7_frame.pack()

        self.totaling_frame.pack()

        self.item1_label.pack(side = 'left')
        self.print1_button.pack(side = 'right')

        self.item2_label.pack(side = 'left')
        self.print2_button.pack(side = 'right')

        self.item3_label.pack(side = 'left')
        self.print3_button.pack(side = 'right')

        self.item4_label.pack(side = 'left')
        self.print4_button.pack(side = 'right')

        self.item5_label.pack(side = 'left')
        self.print5_button.pack(side = 'right')

        self.item6_label.pack(side = 'left')
        self.print6_button.pack(side = 'right')

        self.item7_label.pack(side = 'left')
        self.print7_button.pack(side = 'right')
        

        self.totalcost_label.pack()



        tkinter.mainloop()

    def addservice(self, serviceprice):
        global totalservicecost
        totalservicecost += serviceprice
        label = 'Total service cost : $' + format(totalservicecost,'.2f')
        self.totalservices.set(label)


my_gui = CustomerInterface()



