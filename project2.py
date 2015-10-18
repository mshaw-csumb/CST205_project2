import audioop
import wave
import struct
import array
import binascii
import pydub
from pydub import AudioSegment

def main():
    wave_read_pg =  wave.open("sez.wav",'r')#read the file we want
    frame_count = wave_read_pg.getnframes()#get the number of frames
    print("Number of Frames: %d" % frame_count)#debugging purposes

    frameRate = wave_read_pg.getframerate()#get the framerate, ie audio quality, cd, mp3, etc..

    print("frame rate: %d" % frameRate)#debugging

    framesList = wave_read_pg.readframes(frame_count)#get all the values of each sample in each frame

    wr = wave.open("test4.wav",'wb')#open a new file, this file will be created with this name
    wr.setframerate(frameRate*2)#set the framerate this framerate causes file to be deeper, slower sounding. multiplying rate by 2 fixes this.
    #some informati0n may be lost in the process of converting the hex, or the frameRate is somehow wrong

    #print(framesList)

    sampleWidth = wave_read_pg.getsampwidth()#set the sample width, (how many bits the sound is represented in0
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





main()