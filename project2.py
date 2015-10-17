import audioop
import wave
import pydub
from pydub import AudioSegment

def main():
    #AudioSegment.ffmpeg = "c:\\ffmpeg\\bin\\ffmpeg.exe" not needed, doesn't work anyway
    pg = AudioSegment.from_wav("C:\\Users\Markus\School\CST 205\projects\project2\ey_b0ss.wav")
    pg_reverse = pg.reverse()
    pg_reverse.export("C:\\Users\Markus\School\CST 205\projects\project2\\reverse_b0ss.wav", format="wav")


main()