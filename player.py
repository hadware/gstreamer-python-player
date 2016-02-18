import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst, Gtk

# Initializing threads used by the Gst various elements
GObject.threads_init()
#Initializes the GStreamer library, setting up internal path lists, registering built-in elements, and loading standard plugins.
Gst.init(None)

class Main:
    def __init__(self):
        self.mainloop = GObject.MainLoop()
        #Creating the gst pipeline we're going to add elements to and use to play the file
        self.pipeline = Gst.Pipeline.new("mypipeline")

        #creating the filesrc element, and adding it to the pipeline
        self.filesrc = Gst.ElementFactory.make("filesrc", "filesrc")
        self.filesrc.set_property("location", """/path/to/mysoundfile.mp3""")
        self.pipeline.add(self.filesrc)
        
        #creating and adding the decodebin element , an "automagic" element able to configure itself to decode pretty much anything
        self.decode = Gst.ElementFactory.make("decodebin", "decode")
        self.pipeline.add(self.decode)
        #connecting the decoder's "pad-added" event to a handler: the decoder doesn't yet have an output pad (a source), it's created at runtime when the decoders starts receiving some data
        self.decode.connect("pad-added", self.decode_src_created) 
        
        #setting up (and adding) the alsasin, which is actually going to "play" the sound it receives
        self.sink = Gst.ElementFactory.make("alsasink", "sink")
        self.pipeline.add(self.sink)

        #linking elements one to another (here it's just the filesrc - > decoder link , the decoder -> sink link's going to be set up later)
        self.filesrc.link(self.decode)
            
    #handler taking care of linking the decoder's newly created source pad to the sink
    def decode_src_created(self, element, pad):
        pad.link(self.sink.get_static_pad("sink"))
        
    #running the shit
    def run(self):
        self.pipeline.set_state(Gst.State.PLAYING)
        self.mainloop.run()

start=Main()
start.run()
