FROM ubuntu

RUN apt-get update && apt-get install -y sudo
RUN sudo apt-get install -y \
    python3.8 \
    python3-pip \
    git \
    vim

RUN cd usr/src/
RUN git clone https://github.com/dnplab/odnplab
RUN cd odnplab
RUN pip install -r requirements.txt

RUN alias python=python3.8
RUN alias pip=pip3
