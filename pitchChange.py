__author__ = 'Markus'
__name__ = 'pitchChange'

def makeLow(framerate):
    framerate-= framerate//2
    return framerate

def makeHigh(framerate):
    framerate+= framerate//2
    return framerate
