import wave
import pitchChange
from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
welcomeLabel = Label(topFrame, text="Welcome to Pitch a Tempo")
label1 = Label(topFrame,text="Enter a fileName: ")
fileEntry = Entry(topFrame)
button1 = Button(bottomFrame, text="Higher Pitch", fg="red")
button2 = Button(bottomFrame, text="Lower Pitch", fg="blue")
before = Button(bottomFrame, text="Before", fg="green")
after = Button(bottomFrame, text="After", fg="orange")
button4 = Button(bottomFrame, text="Exit Program", fg="purple", command = exit)

welcomeLabel.pack()
label1.pack(side=LEFT)
fileEntry.pack(side = RIGHT)
button1.pack()
button2.pack()
before.pack()
after.pack()

#button3.pack()
button4.pack()

root.mainloop()#must be run when your application is ready to be run


def main():
    filename = fileEntry.get()
    originalFile =  wave.open(filename,'r')#read the file we want
