#!/usr/bin/env python

import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst
import os

Gst.init()
mainloop = GObject.MainLoop()

#setting up a single "playbin" element which handles every part of the playback by itself
pl = Gst.ElementFactory.make("playbin", "player")
# copy a track to /tmp directory, just for testing
pl.set_property('uri','file://'+os.path.abspath('/tmp/track.ogg'))
# setting the volume property for the playbin element, as an example
pl.set_property('volume', 0.2)

#running the playbin 
pl.set_state(Gst.State.PLAYING)
mainloop.run()
