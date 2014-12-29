gstreamer-python-player
=======================

Various examples of minimalist music players in python, using the new Gstreamer 1.0 API. 
The point is to cover by example the following implementations using Gstreamer 1.0 and the GTK+3 API:
* Pipeline usage
* Use a full "read -> decode -> output to sink" pipeline
* Simply play an audio file using gstreamer and python
* Use a slider to display the stream's current playback position, and change it

## player.py

A simple python conversion of the following bash gstreamer command:
```bash
    gst-launch-1.0 filesrc location="/path/to/your/file.mp3" ! decodebin ! alsasink
```

It doesn't contain any graphical elements (no Gtk window or else). There is a small catch here: the decodebin doesn't have a source pad before startup, thus, we cannot connect it to the sink before it's been fed with a stream. We have to wait for it to create its output pad, signal it, and then handler the signal event to connect the pad to the sink's pad

## player_minimal.py 

Instead of a "full" pipeline, here it's just an example of some adapted code from [this page](http://codeboje.de/playing-mp3-stream-python/ ). It uses the "playbin" element which condenses all the elements from the player.py example into one automagic element.

## seek.py 

Mainly a translation and simplification of [this code](http://codeboje.de/playing-mp3-stream-python/)
The simplest possible example of a sound player: a "Play" button, a "Pause" button, and a slider to control the playback position. It makes usage of controls signals to start at stop the element's playback state, and uses a Glib timer to check on the current position of the stream. When the slider is manually moved, it also makes use of the seek_simple() function to seek in the stream.

You should probably use the [official doc](http://lazka.github.io/pgi-docs/index.html) as well as the [gstreamer1.0 porting tutorial](https://wiki.ubuntu.com/Novacut/GStreamer1.0) to start using the gstreamer1.0 API while feeding on gst0.10-based examples.

