#!/usr/bin/env python

import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst, Gtk
import os

Gst.init()
mainloop = GObject.MainLoop()

#setting up a single "playbin" element which handles every part of the playback by itself
pl = Gst.ElementFactory.make("playbin", "player")
pl.set_property('uri','file://'+os.path.abspath('/tmp/lea.mp3'))

#running the playbin 
pl.set_state(Gst.State.PLAYING)
mainloop.run()
