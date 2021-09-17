FROM xyzt-dev:kinect

USER root
RUN \
  apt install -y \
  libfftw3-dev libconfig-dev libasound2-dev \
  alsa-utils alsa-base

RUN usermod -aG audio docker

USER docker