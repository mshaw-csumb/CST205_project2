#the following code was found from https://markwingerd.wordpress.com/2014/11/19/using-gstreamer-with-python/
#it is meant as a test of gstreamer it is using gstreamer to pleay an mp3 named s.mp3 which is
#a mashup of Solitaire and I'm a ruin by Marina and the Diamonds, that was acquired from youtube
import pygst
pygst.require("0.10")
import gst
import audioop
import gi

print("hello world ")

pipeline = gst.Pipeline('pipeline')

audio_source = gst.element_factory_make('filesrc', 'audio_source')
decode = gst.element_factory_make('mad','decode')
convert = gst.element_factory_make('audioconvert', 'convert')
equalizer = gst.element_factory_make('equalizer-3bands', 'equalizer')
audio_sink = gst.element_factory_make('autoaudiosink', 'audio_sink')


if (not pipeline or not audio_source or not decode or not convert or
    not equalizer or not audio_sink):
    print 'Not all elements could be created.'
    exit(-1)

# Configure our elements.
audio_source.set_property('location', 's.mp3')
equalizer.set_property('band1', -24.0)
equalizer.set_property('band2', -24.0)

# Add our elements to the pipeline.
pipeline.add(audio_source, decode, convert, equalizer, audio_sink)

# Link our elements together.
if (not gst.element_link_many(audio_source, decode, convert, equalizer, audio_sink)):
    print "Elements could not be linked."
    exit(-1)

# Set our pipelines state to Playing.
pipeline.set_state(gst.STATE_PLAYING)

# Wait until error or EOS.
bus = pipeline.get_bus()
msg = bus.timed_pop_filtered(gst.CLOCK_TIME_NONE,
    gst.MESSAGE_ERROR | gst.MESSAGE_EOS)
print msg

op = input("1 for pause")
if(op == 1):
    pipeline.set_state(gst.STATE_PAUSED)
# Free resources.
pipeline.set_state(gst.STATE_NULL)