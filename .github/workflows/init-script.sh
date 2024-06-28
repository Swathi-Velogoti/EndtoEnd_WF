#!/bin/bash
# Update and install necessary packages
sudo apt update -y
sudo apt install -y python3-venv python3-pip

# Create a virtual environment and install Flask
python3 -m venv venv
source venv/bin/activate
pip install Flask

# Deactivate the virtual environment
deactivate
