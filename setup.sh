#!/bin/sh
sudo apt update
sudo apt install python3-pip
git clone https://github.com/dnplab/odnplab
pip install dnplab
pip install streamlit==0.65.2
