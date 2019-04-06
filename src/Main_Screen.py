# Simple enough, just import everything from tkinter.
from tkinter import *


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Timing Screen")

        #the car labels with the numbers
        Car1 = Label(root, text="1  ", relief=RIDGE, bg="grey").grid(row=0, sticky=W+N)
        Car2 = Label(root, text="2  ", relief=RIDGE, bg="grey").grid(row=1, sticky=W+N)
        Car3 = Label(root, text="3  ", relief=RIDGE, bg="grey").grid(row=2, sticky=W+N)
        Car4 = Label(root, text="4  ", relief=RIDGE, bg="grey").grid(row=3, sticky=W+N)
        Car5 = Label(root, text="5  ", relief=RIDGE, bg="grey").grid(row=4, sticky=W+N)
        Car6 = Label(root, text="6  ", relief=RIDGE, bg="grey").grid(row=5, sticky=W+N)
        Car7 = Label(root, text="7  ", relief=RIDGE, bg="grey").grid(row=6, sticky=W + N)
        Car8 = Label(root, text="8  ", relief=RIDGE, bg="grey").grid(row=7, sticky=W+N)
        Car9 = Label(root, text="9  ", relief=RIDGE, bg="grey").grid(row=8, sticky=W+N)
        Car10 = Label(root, text="10", relief=RIDGE, bg="grey").grid(row=9, sticky=W+N)
        Car11 = Label(root, text="11", relief=RIDGE, bg="grey").grid(row=10, sticky=W+N)
        Car12 = Label(root, text="12", relief=RIDGE, bg="grey").grid(row=11, sticky=W+N)

        #the text box to write the team name in
        e1 = Entry(root).grid(row=0, column=1, sticky=W+N)
        e2 = Entry(root).grid(row=1, column=1, sticky=W + N)
        e3 = Entry(root).grid(row=2, column=1, sticky=W + N)
        e4 = Entry(root).grid(row=3, column=1, sticky=W + N)
        e5 = Entry(root).grid(row=4, column=1, sticky=W + N)
        e6 = Entry(root).grid(row=5, column=1, sticky=W + N)
        e7 = Entry(root).grid(row=6, column=1, sticky=W + N)
        e8 = Entry(root).grid(row=7, column=1, sticky=W + N)
        e9 = Entry(root).grid(row=8, column=1, sticky=W + N)
        e10 = Entry(root).grid(row=9, column=1, sticky=W + N)
        e11 = Entry(root).grid(row=10, column=1, sticky=W + N)
        e12 = Entry(root).grid(row=11, column=1, sticky=W + N)

        #Lap button
        lap_button1 = Button(root, text="Lap").grid(row=0, column=2, sticky=W+N)
        lap_button2 = Button(root, text="Lap").grid(row=1, column=2, sticky=W + N)
        lap_button3 = Button(root, text="Lap").grid(row=2, column=2, sticky=W + N)
        lap_button4 = Button(root, text="Lap").grid(row=3, column=2, sticky=W + N)
        lap_button5 = Button(root, text="Lap").grid(row=4, column=2, sticky=W + N)
        lap_button6 = Button(root, text="Lap").grid(row=5, column=2, sticky=W + N)
        lap_button7 = Button(root, text="Lap").grid(row=6, column=2, sticky=W + N)
        lap_button8 = Button(root, text="Lap").grid(row=7, column=2, sticky=W + N)
        lap_button9 = Button(root, text="Lap").grid(row=8, column=2, sticky=W + N)
        lap_button10 = Button(root, text="Lap").grid(row=9, column=2, sticky=W + N)
        lap_button11 = Button(root, text="Lap").grid(row=10, column=2, sticky=W + N)
        lap_button12 = Button(root, text="Lap").grid(row=11, column=2, sticky=W + N)

    def end_program(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
#root.geometry("600x700")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()