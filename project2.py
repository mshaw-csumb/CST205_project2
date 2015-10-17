import audioop
import wave
import struct
import array
import pydub
from pydub import AudioSegment

def main():
    #AudioSegment.ffmpeg = "c:\\ffmpeg\\bin\\ffmpeg.exe" not needed, doesn't work anyway
   # pg = AudioSegment.from_wav("ey_b0ss.wav")
    #pg_reverse = pg.reverse()
   # pg_reverse.export("reverse_b0ss.wav", format="wav")

    wave_read_pg =  wave.open("ey_b0ss.wav",'r')
    frame_count = wave_read_pg.getnframes()
    print(frame_count)

    frameRate = wave_read_pg.getframerate()

    print(frameRate)

    framesList = wave_read_pg.readframes(frame_count)


    print(framesList)

    sampleWidth = wave_read_pg.getsampwidth()
    print(sampleWidth)

    #sample_array = struct.unpack("<H",framesList[0:1)
    #print(sample_array)
    #for k in range(0,frame_count):
    #    framesList[k]+= 10
    #print(framesList)

main()