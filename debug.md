## Issue:
```
/home/docker/catkin_ws/src/odas_ros/odas_ros/odas_ros/odas/config/kinect.cfg:265 - syntax error
```

## Fix:
comment out a line that shouldn't be there

## Issue:
```
ALSA lib pcm_hw.c:1700:(_snd_pcm_hw_open) Invalid value for card
Source hops: Cannot open audio device hw:1,0: No such file or directory
```

## Fix:
Put in udev rules
```
SUBSYSTEM=="usb", ATTRS{idVendor}=="045e", MODE:="0666", TAG+="uaccess", TAG+="udev-acl"
```
in `/etc/udev/rules.d/azure.rules`

Install ALSA `sudo apt install alsa-utils alsa-base`

add user to audio `sudo usermod -aG audio docker` (username is `docker`)

run `arecord -l` and take note of which id Kinect. Place that in the cfg.

## Issue:
Seems to be nothing on publish

## Fix:
unknown. Test in audacity. Increase gain. Re-enable socket
Try logging to json in tracks and potential in order to verify the issue is with the webserver.
```
        # interface: {
        #     type = "file";
        #     path = "/home/docker/potential.json";
        # }
```

## Issue:
After running for some time, crashes
```
[odas_core_node-3] process has died [pid 554, exit code -11, cmd /home/docker/catkin_ws/devel/lib/odas_ros/odas_core_node __name:=odas_core_node __log:=/home/docker/.ros/log/6e76b818-8da2-11eb-8c21-0242ac110002/odas_core_node-3.log].
log file: /home/docker/.ros/log/6e76b818-8da2-11eb-8c21-0242ac110002/odas_core_node-3*.log
```