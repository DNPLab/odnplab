FROM ubuntu

RUN apt-get update && apt-get install -y sudo
RUN sudo apt-get install -y \
    python3.8 \
    python3-pip \
    git \
    vim

RUN alias python=python3.8
RUN alias pip=pip3
