import audioop
import wave
import array
import tkinter
import tkinter.messagebox


def main():

    print("Welome to Pitch a Tempo\n")

    #filename = input("Enter the name, make sure it is a wav file: ")
    originalFile =  wave.open("C:/Users/Bryant/PycharmProjects/untitled/CST205_project2/sez.wav",'r')#read the file we want


    while(not(input==3)):
        printMenu()#printMenu
        choice = input("make your choice: ")
        frame_count =originalFile.getnframes()#get the number of frames
        frameRate =originalFile.getframerate()#get the framerate, ie audio quality, cd, mp3, etc..
        framesList =originalFile.readframes(frame_count)#get all the values of each sample in each frame

        frameRate*=2
        print("Number of Frames: %d" % frame_count)#debugging purposes
        print("frame rate: %d" % frameRate)#debugging


        if(choice == "1"):#make deeper
            frameRate = makeLow(frameRate)
        elif(choice == "2"):
            frameRate = makeHigh(frameRate)
        elif(choice == "3"):
            exit(0)
        print("Modified framerate: %d" % frameRate)
        outputFileName = input("Enter an output file name: ")
        wr = wave.open(outputFileName,'wb')#open a new file, this file will be created with this name
        wr.setframerate(frameRate)#set the framerate this framerate causes file to be deeper, slower sounding. multiplying rate by 2 fixes this.
        #some informati0n may be lost in the process of converting the hex, or the frameRate is somehow wrong

        #print(framesList)

        sampleWidth =originalFile.getsampwidth()#set the sample width, (how many bits the sound is represented in0
        print("Sample width: %d bits"  % sampleWidth )
        samples = array.array('B',framesList)#turn the list of frame values into a byte array, converting hex into a number we can do math on
        #print(samples)


        # print(samples)
        #samplesString = '\\x'.join('{:02x}'.format(x) for x in samples)
        #print(''.join('{:02x}'.format(x) for x in samples))
        #print(samplesString)
        wr.setnchannels(1)#set the number of channels, 1 for mono, 2 for stereo
        wr.setnframes(frame_count)#set the number of frames for this file
        wr.setsampwidth(2)#set the sample width, (bit representation of sound)
        wr.writeframes(samples)#write the byte array to this new file,
        wr.close()#close the file and it should be a playable .wav file

        #print("From byte array to hex string is what is above")

def printMenu():
    print("What do you want to do with this file?")
    print("1\tMake the audio deeper (this will make duration of the file longer)")
    print("2\tMake the audio higher (this will make the duration of the file shorter)")
    print("3\tExit program")

def makeLow(framerate):
    framerate-= framerate//2
    return framerate

def makeHigh(framerate):
    framerate+= framerate//2
    return framerate

main()