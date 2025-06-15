#!/bin/bash

# docker build . -t xameeramir/cra-docker
docker build . -t fpaa-python-rust

docker run fpaa-python-rust