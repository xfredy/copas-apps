#!/bin/bash

wait_for_xfce()
{
    while [ ! -d "/root/Desktop/" ]
    do
        sleep 1
    done
    # 16:9 aspect ratio
    xrandr --newmode "856x480_60.00"  31.73  856 872 960 1064  480 481 484 497  -HSync +Vsync  -HSync +Vsync && xrandr --addmode screen "856x480_60.00"
    xrandr --newmode "1280x720_60.00"  74.48  1280 1336 1472 1664  720 721 724 746  -HSync +Vsync && xrandr --addmode screen "1280x720_60.00"
    # 4:3 aspect ratio
    xrandr --newmode "800x600_60.00"  38.22  800 832 912 1024  600 601 604 622  -HSync +Vsync && xrandr --addmode screen "800x600_60.00"
    xrandr --newmode "1280x960_60.00"  102.10  1280 1360 1496 1712  960 961 964 994  -HSync +Vsync && xrandr --addmode screen "1280x960_60.00"
}

set -e

cd /copas-ui && gunicorn "app:create_app()" &
cd /copas-app && gunicorn "app:app" &

Xvfb :20 -screen 0 1920x1080x24 >/dev/null 2>/dev/null &
x11vnc -display :20 -repeat -shared -forever -rfbport 5900 >/dev/null 2>/dev/null &
/noVNC/utils/novnc_proxy --listen 8081 --vnc localhost:5900 >/dev/null 2>/dev/null &
wait_for_xfce &
exec xfce4-session --display=:20

