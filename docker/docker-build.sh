#!/bin/bash

DOCKER_DIR=$(readlink -f $(dirname $0))
docker build -t xyzt-dev:odas $DOCKER_DIR
