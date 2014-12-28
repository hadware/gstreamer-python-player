#!/usr/bin/env python
import pygst
pygst.require('0.10')
import gst
import gobject
import os

mainloop = gobject.MainLoop()
#setting up a single "playbin" element which handles every part of the playback by itself
pl = gst.element_factory_make("playbin", "player")
pl.set_property('uri','file://'+os.path.abspath('/tmp/lea.mp3'))

#running the playbin 
pl.set_state(gst.STATE_PLAYING)
mainloop.run()
