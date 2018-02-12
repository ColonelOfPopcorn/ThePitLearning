from tkinter import *
from PIL import Image, ImageTk
from random import randint

#create class (window) and inherit from the class (Frame)
#Frame is a class imported from tkinter (Lib/tkinter/__init__)
class Window(Frame):

    #initializing the main window
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        #changing the title of Master Widget
        self.master.title("The Test")

        #allowing the widget to take the full space of the root(main) window aka Frame
        self.pack(fill=BOTH, expand=1)

        #create a Menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        #setting up File menu and Exit command
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        #setting up Edit menu and some test commands
        edit = Menu(menu)
        edit.add_command(label="Show Image", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)
        menu.add_cascade(label="Edit", menu=edit)

        #creating the button instance
        rollButton = Button(self, text="Roll 3d6",command=diceroll(3,6))

        #placing the button in the window
        rollButton.place(x=0, y=0)

    def showImg(self):
        load = Image.open("chat.png")
        render = ImageTk.PhotoImage(load)

        #labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

    def client_exit(self):
        exit()

def diceroll(number, sides):
    result = 0
    for x in range(0,number):
        roll = randint(1,sides)
        result = result + roll
    return result

def dicemenu():
    print("How many dice would you like to roll?")
    qloop = 1
    while qloop:
        try:
            quantity = int(input())
            qloop=0
        except ValueError:
            print("That's not a number, please try again.")
        
    print("How many sides are on your dice?")
    sloop = 1
    while sloop:
        try:
            numberofsides = int(input())
            sloop = 0
        except ValueError:
            print("That's not a number, please try again.")

    print("Your result is: ",diceroll(quantity,numberofsides))

def intro():
    print("Welcome to The Test. This is Placeholder text.")

def main():
    repeat = True

    while repeat:
        print("What would you like to do?")
        commandinput = input().lower()
        command = commandinput.split()
        print("DEBUG: ",command)
        #below will cause a crash if there isn't at least one space in the input, since the split command fails
        if command[1] == "/roll":
            dicemenu()
        if command[1] == "/debug":
            print("placeholder debug menu")
        

        print("Would you like to continue? y/n")
        repeat = ("y" or "yes") in input().lower()

#root window (frame) created.
root = Tk()

#size of the window
root.geometry("400x300")

#creation of an instance. Presumably multiple instances can exist
app = Window(root)
root.mainloop()
