#!/bin/bash

# start xpra as xpra user with command specified in dockerfile as CMD or passed as parameter to docker run
CMD="XPRA_PASSWORD=$XPRA_PASSWORD /usr/bin/xpra start-desktop --daemon=no --start-child='$@'"
runuser -l xpra -c "$CMD"
XPRA_PASSWORD=123 xpra start-desktop --bind-tcp=0.0.0.0:10000 --html=on --start-child=xterm --exit-with-children=no --daemon=no --notifications=no --bell=no :100


#xpra start-desktop --bind-tcp=0.0.0.0:9876 --html=on --start-child=gnome-terminal --exit-with-children=no --daemon=no --xvfb="/usr/bin/Xvfb +extension Composite -screen 0 1920x1080x24+32  -nolisten tcp -noreset" --pulseaudio=no --notifications=no --bell=no :100