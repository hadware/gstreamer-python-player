gstreamer-python-player
=======================

A minimalist music player in python, using the new Gstreamer 1.0 API. 
The point is to show an example of the following actions using Gstreamer 1.0 and the GTK+3 API:
* Use a pipeline
* Use a full "read -> decode -> concert -> output to sink" element line
* Simply play some sound using gstreamer and python

I also copied in some code from http://codeboje.de/playing-mp3-stream-python/ to make an even simpler , but in my opinion much less instructive, example.

You should probably use the [official doc](http://lazka.github.io/pgi-docs/index.html) as well as the [gstreamer1.0 porting tutorial](https://wiki.ubuntu.com/Novacut/GStreamer1.0) to start using the gstreamer1.0 API while feeding on gst0.10-based examples.

