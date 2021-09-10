FROM xyzt-dev:20-latest

USER root
RUN \
  apt update && \
  apt upgrade -y && \
  apt install -y \
  libfftw3-dev libconfig-dev libasound2-dev \
  alsa-utils alsa-base

RUN mkdir -p /etc/udev/rules.d && \
    echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="045e", MODE:="0666", TAG+="uaccess", TAG+="udev-acl"' > /etc/udev/rules.d/azure.rules

RUN usermod -aG audio docker

USER docker