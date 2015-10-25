import audioop
import wave
import array
import winsound
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox


frameRate = 0

def printLabel(testLabel):
    testLabel.config(text = "Button 1 pressed")

def main():

    root = Tk()
    w = Label(root, text="Pitch a Tempo")
    w.pack()

    tkinter.messagebox.showinfo("Greetings!","Welcome to Pitch a Tempo")

    global filename
    filename = tkinter.simpledialog.askstring("File", "add file name, must be wav file")

    topFrame = Frame(root)
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    #testLabel = Label(topFrame, text="")
    welcomeLabel = Label(topFrame, text="Welcome to Pitch a Tempo")

    #get the file
    global label1
    label1 = Label(topFrame,text="Enter an output fileName: ")

    global fileEntry
    fileEntry = Entry(topFrame)
    #open the file
    originalFile =  wave.open(filename,'r')#read the file we want

    #get attributes of the file
    global frame_count
    frame_count =originalFile.getnframes()#get the number of frames
    global frameRate
    frameRate =originalFile.getframerate()#get the framerate, ie audio quality, cd, mp3, etc..
    global framesList
    framesList =originalFile.readframes(frame_count)#get all the values of each sample in each frame

    frameRate*=2

    button1 = Button(bottomFrame, text="Higher Pitch", fg="red",command = makeHigh)
    button2 = Button(bottomFrame, text="Lower Pitch", fg="blue",command = makeLow)
    before = Button(bottomFrame, text="Before", fg="green", command = playBefore)#play original file
    after = Button(bottomFrame, text="After", fg="orange",command = playAfter)#play new file name
    button4 = Button(bottomFrame, text="Exit Program", fg="purple", command = exit)
    welcomeLabel.pack()
    label1.pack(side=LEFT)
    fileEntry.pack(side = RIGHT)

    button1.pack()
    button2.pack()
    before.pack()
    after.pack()
    root.mainloop()
    #button3.pack()
    button4.pack()

    #originalFile =  wave.open(filename,'r')#read the file we want

    #printMenu()#printMenu
    #choice = input("make your choice: ")


    #print("Number of Frames: %d" % frame_count)#debugging purposes
    #print("frame rate: %d" % frameRate)#debugging

    """
    if(choice == "1"):#make deeper
        frameRate = makeLow(frameRate)
    elif(choice == "2"):
       frameRate = makeHigh(frameRate)
    print("Modified framerate: %d" % frameRate)

    outputFileName = input("Enter an output file name: ")

    wr = wave.open(outputFileName,'wb')#open a new file, this file will be created with this name
    wr.setframerate(frameRate)#set the framerate this framerate causes file to be deeper, slower sounding. multiplying rate by 2 fixes this.
    #some informati0n may be lost in the process of converting the hex, or the frameRate is somehow wrong

    #print(framesList)
    """
    #sampleWidth =originalFile.getsampwidth()#set the sample width, (how many bits the sound is represented in0
    #print("Sample width: %d bits"  % sampleWidth )
    #samples = array.array('B',framesList)#turn the list of frame values into a byte array, converting hex into a number we can do math on
    #print(samples)


    # print(samples)
    #samplesString = '\\x'.join('{:02x}'.format(x) for x in samples)
    #print(''.join('{:02x}'.format(x) for x in samples))
    #print(samplesString)


    #print("From byte array to hex string is what is above")

def printMenu():
    print("What do you want to do with this file?")
    print("1\tMake the audio deeper (this will make duration of the file longer")
    print("2\tMake the audio higher (this will make the duration of the file shorter")

def makeLow():
    global frameRate
    frameRate-= frameRate//2
    #return frameRate
    writeFile()

def makeHigh():
    global frameRate
    frameRate+= frameRate//2
    #return frameRate
    writeFile()

def playBefore():
    winsound.PlaySound(filename,winsound.SND_FILENAME)

def playAfter():
    winsound.PlaySound(outputFileName,winsound.SND_FILENAME)

def writeFile():
    global wr
    global frame_count
    global samples
    global frameList
    global frameRate
    global outputFileName
    outputFileName = fileEntry.get()
    wr = wave.open(outputFileName,'wb')#open a new file, this file will be created with this name
    wr.setframerate(frameRate)
    wr.setnchannels(1)#set the number of channels, 1 for mono, 2 for stereo
    wr.setnframes(frame_count)#set the number of frames for this file
    wr.setsampwidth(2)#set the sample width, (bit representation of sound)
    wr.writeframes(framesList)#write the byte array to this new file,
    wr.close()#close the file and it should be a playable .wav file

main()